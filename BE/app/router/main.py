from fastapi import APIRouter, HTTPException, Depends,WebSocket, WebSocketDisconnect,File,UploadFile
from sqlalchemy.orm import Session
from typing import List,Dict
from app.db import create_session
from app.models.data.main import QuartiereProposalModel
from app.models.schemas.main import QuartiereProposalCreate, QuartiereProposalUpdate, QuartiereProposalRead, QuartiereProposalList, QuartiereProposalDelete
from app.my_agent.agent import ProposalCatcherAgent  
from app.services.proposal import row_to_proposal,generate_labels
import json
import pandas as pd
import numpy as np
from io import StringIO
from app.my_agent.rag import RAGChromaPipeline
from app.my_agent.groq_v2 import GroqLlama


llm=GroqLlama()
router = APIRouter()
rag_pipeline = RAGChromaPipeline()

# Route to create a new QuartiereProposal
@router.post("/quartiere_proposals/", response_model=QuartiereProposalRead)
def create_proposal(proposal: QuartiereProposalCreate, db: Session = Depends(create_session)):
    db_proposal = QuartiereProposalModel(**proposal.dict())
    db.add(db_proposal)
    db.commit()
    db.refresh(db_proposal)
    return db_proposal

# Route to get a single QuartiereProposal by ID
@router.get("/quartiere_proposals/{proposal_id}", response_model=QuartiereProposalRead)
def get_proposal(proposal_id: int, db: Session = Depends(create_session)):
    db_proposal = db.query(QuartiereProposalModel).filter(QuartiereProposalModel.id == proposal_id).first()
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return db_proposal

# Route to get a list of QuartiereProposals
@router.get("/quartiere_proposals/", response_model=QuartiereProposalList)
def list_proposals(db: Session = Depends(create_session)):
    proposals = db.query(QuartiereProposalModel).all()
    return QuartiereProposalList(proposals=proposals)

# Route to update an existing QuartiereProposal by ID
@router.put("/quartiere_proposals/{proposal_id}", response_model=QuartiereProposalRead)
def update_proposal(proposal_id: int, proposal: QuartiereProposalUpdate, db: Session = Depends(create_session)):
    db_proposal = db.query(QuartiereProposalModel).filter(QuartiereProposalModel.id == proposal_id).first()
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    for key, value in proposal.dict(exclude_unset=True).items():
        setattr(db_proposal, key, value)
    db.commit()
    db.refresh(db_proposal)
    return db_proposal

# Route to delete a QuartiereProposal by ID
@router.delete("/quartiere_proposals/{proposal_id}", response_model=QuartiereProposalDelete)
def delete_proposal(proposal_id: int, db: Session = Depends(create_session)):
    db_proposal = db.query(QuartiereProposalModel).filter(QuartiereProposalModel.id == proposal_id).first()
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    db.delete(db_proposal)
    db.commit()
    return QuartiereProposalDelete(id=proposal_id)


@router.post("/ingest_csv/")
async def ingest_csv(db: Session = Depends(create_session),file: UploadFile = File(...)):
    try:
        contents = await file.read()
        print("File contents (first 100 chars):", contents[:100])
        try:
            s = contents.decode('utf-8')
        except UnicodeDecodeError as decode_err:
            raise HTTPException(status_code=400, detail=f"File encoding not supported, please use UTF-8. Error: {str(decode_err)}")
        try:
            data = pd.read_csv(StringIO(s), delimiter=';')
        except pd.errors.ParserError as parse_err:
            raise HTTPException(status_code=400, detail=f"Error parsing CSV data: {str(parse_err)}")
        data = data.replace({np.nan: ''}).astype(str)
        proposals = [row_to_proposal(row) for _, row in data.iterrows()]
        for proposal in proposals:
            db_proposal = QuartiereProposalModel(**proposal.dict())
            db.add(db_proposal)
            db.commit()
            db.refresh(db_proposal)
            rag_pipeline.ingest_text(proposal.proposal,"Bologna")
        return proposals
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")



user_states: Dict[str, dict] = {}

@router.post("/process_state")
def process_state():
    # Esegui il grafo con lo stato fornito
    state={
        "messages": [],
        "nome_proposta": None,
        "quartiere": None,
        "zona_prossimita": None,
        "proposal": None,
        "labels": None
    }
    current_state = ProposalCatcherAgent().graph.invoke(state)
    return current_state

@router.websocket("/chat/citizen")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    user_id = str(id(websocket))  # Puoi usare un ID più sofisticato per ogni utente
    user_states[user_id] = {
        "messages": [],
        "nome_proposta": None,
        "quartiere": None,
        "zona_prossimita": None,
        "proposal": None,
        "labels": None
    }
    main_prompt="Sei un assistente della pubblica amministrazione e il tuo obiettivo è quello di ascoltare i cittadini come rappresentanti dei quartieri per il miglioramento della città. Il tuo obiettivo è raccogliere informazioni sulle proposte di miglioramento che loro vogliono portare alla città e alla visione della pubblica amministrazione."

    try:
        while True:
            # Attendi il messaggio dell'utente
            state = user_states[user_id]
            if state["messages"].__len__() == 0:
                updated_state = ProposalCatcherAgent().graph.invoke(state)
                user_states[user_id] = updated_state
                bot_message = updated_state["messages"][-1]["content"]
                await websocket.send_text(bot_message)
            else:
                user_message = await websocket.receive_text()
                if not state.get("nome_proposta"):
                    proposal = llm(task_type="completion",completion_prompt=""+main_prompt+" Valuta questo message e estrai il nome della proposta: "+user_message+" Se non è presente il nome della proposta scrivi 'Non presente' se presente ritorna il nome della proposta")
                    if proposal == "Non presente":
                        proposal = None
                    updated_state = user_states[user_id]
                    updated_state["nome_proposta"] = proposal
                    user_states[user_id] = updated_state    
                
                elif not state.get("quartiere"):
                    quartiere = llm(task_type="completion",completion_prompt=""+main_prompt+" Valuta questo message e estrai il nome del quartiere: "+user_message+" Se non è presente il nome del quartiere scrivi 'Non presente' se presente ritorna il nome del quartiere")
                    if quartiere == "Non presente":
                        quartiere = None
                    updated_state = user_states[user_id]
                    updated_state["quartiere"] = quartiere
                    user_states[user_id] = updated_state 
                elif not state.get("proposal"):
                    proposal = llm(task_type="completion",completion_prompt=""+main_prompt+" Valuta questo message e estrai la proposta: "+user_message+" Se non sei soddisfatto della proposta scrivi 'Non presente'  Se sei soddisfatto della proposta scrivi la proposta")
                    if proposal == "Non presente":
                        proposal = None
                    updated_state = user_states[user_id]
                    updated_state["proposal"] = proposal
                    user_states[user_id] = updated_state
                
                # Aggiorna lo stato dell'utente con il nuovo messaggio
                state = user_states[user_id]
                state["messages"].append({"role": "user", "content": user_message})

                # Esegui il workflow
                updated_state = ProposalCatcherAgent().graph.invoke(state)

                # Aggiorna lo stato utente con lo stato aggiornato dal workflow
                user_states[user_id] = updated_state

                # Ottieni la risposta del bot dal workflow
                bot_message = updated_state["messages"][-1]["content"]

                # Invia la risposta al frontend
                await websocket.send_text(bot_message)

    except WebSocketDisconnect:
        # Rimuovi lo stato dell'utente quando si disconnette
        del user_states[user_id]
        
@router.websocket("/chat/admin")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    user_id = str(id(websocket))  # Puoi usare un ID più sofisticato per ogni utente
    messages = []
    if not rag_pipeline.qa_chain:
        rag_pipeline.create_qa_chain()
    try:
        while True:
            user_message = await websocket.receive_text()

            messages.append({"role": "user", "content": user_message})
            bot_content = rag_pipeline.get_answer(messages[-1].content)
            messages.append({"role": "system", "content": bot_content})
            await websocket.send_text(bot_message)

    except WebSocketDisconnect:
        messages = []