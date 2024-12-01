from fastapi import APIRouter, HTTPException, Depends, WebSocket, WebSocketDisconnect,File,UploadFile
from sqlalchemy.orm import Session
from typing import List, Dict
from app.models.data.wato import Utente, Viaggio, Itinerario, Evento, Chat, Message
from app.models.schemas.wato import UtenteRead, UtenteCreate, ViaggioRead, ViaggioCreate, ItinerarioRead, ItinerarioCreate, EventoRead, EventoCreate, ChatRead, ChatCreate, MessageRead, MessageCreate,StatoViaggio
from app.db import create_session
from app.services.ai_tool import VisionAnalysisService

router = APIRouter()
active_connections: Dict[int, List[WebSocket]] = {}

# Rotte per Utente
@router.post("/utenti/", response_model=UtenteRead)
def create_utente(utente: UtenteCreate, db: Session = Depends(create_session)):
    print(utente)
    db_utente = Utente(nome=utente.nome, email=utente.email, password_hash=utente.password)
    db.add(db_utente)
    db.commit()
    db.refresh(db_utente)
    return db_utente

@router.get("/utenti/{utente_id}", response_model=UtenteRead)
def read_utente(utente_id: int, db: Session = Depends(create_session)):
    utente = db.query(Utente).filter(Utente.id == utente_id).first()
    if utente is None:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    return utente

# Rotte per Viaggio
@router.post("/viaggi/", response_model=ViaggioRead)
def create_viaggio(viaggio: ViaggioCreate, db: Session = Depends(create_session)):
    viaggio_data = viaggio.dict()
    # Converte il valore Enum in stringa se necessario
    if isinstance(viaggio_data['stato'], StatoViaggio):
        viaggio_data['stato'] = viaggio_data['stato'].value.upper()
    print(viaggio_data)
    
    db_viaggio = Viaggio(**viaggio_data)
    db.add(db_viaggio)
    db.commit()
    db.refresh(db_viaggio)
    return ViaggioRead.from_orm(db_viaggio)

@router.get("/viaggi/{viaggio_id}", response_model=ViaggioRead)
def read_viaggio(viaggio_id: int, db: Session = Depends(create_session)):
    viaggio = db.query(Viaggio).filter(Viaggio.id == viaggio_id).first()
    if viaggio is None:
        raise HTTPException(status_code=404, detail="Viaggio non trovato")
    return viaggio

# Rotte per Itinerario
@router.post("/itinerari/", response_model=ItinerarioRead)
def create_itinerario(itinerario: ItinerarioCreate, db: Session = Depends(create_session)):
    db_itinerario = Itinerario(**itinerario.dict())
    db.add(db_itinerario)
    db.commit()
    db.refresh(db_itinerario)
    return db_itinerario

@router.get("/itinerari/{itinerario_id}", response_model=ItinerarioRead)
def read_itinerario(itinerario_id: int, db: Session = Depends(create_session)):
    itinerario = db.query(Itinerario).filter(Itinerario.id == itinerario_id).first()
    if itinerario is None:
        raise HTTPException(status_code=404, detail="Itinerario non trovato")
    return itinerario

# Rotte per Evento
@router.post("/eventi/", response_model=EventoRead)
def create_evento(evento: EventoCreate, db: Session = Depends(create_session)):
    db_evento = Evento(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

@router.get("/eventi/{evento_id}", response_model=EventoRead)
def read_evento(evento_id: int, db: Session = Depends(create_session)):
    evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if evento is None:
        raise HTTPException(status_code=404, detail="Evento non trovato")
    return evento

# Rotte per Chat
@router.post("/chat/", response_model=ChatRead)
def create_chat(chat: ChatCreate, db: Session = Depends(create_session)):
    db_chat = Chat(**chat.dict())
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

@router.get("/chat/{chat_id}", response_model=ChatRead)
def read_chat(chat_id: int, db: Session = Depends(create_session)):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat non trovata")
    return chat

# Rotte per Message
@router.post("/messaggi/", response_model=MessageRead)
def create_message(message: MessageCreate, db: Session = Depends(create_session)):
    db_message = Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    # Notifica tutti i client connessi alla chat
    if message.chat_id in active_connections:
        for connection in active_connections[message.chat_id]:
            connection.send_json({"message": db_message.contenuto, "timestamp": db_message.timestamp.isoformat()})
    return db_message

@router.get("/messaggi/{message_id}", response_model=MessageRead)
def read_message(message_id: int, db: Session = Depends(create_session)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if message is None:
        raise HTTPException(status_code=404, detail="Messaggio non trovato")
    return message

@router.post("/viaggio_ticket/")
def read_message( db: Session = Depends(create_session),images: UploadFile = File(...)):
    test=VisionAnalysisService().analyze_image_with_llama_vision(image)
    return test








# WebSocket per gestire i messaggi in tempo reale e lo stream della chat
@router.websocket("/ws/chat/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    await websocket.accept()
    if chat_id not in active_connections:
        active_connections[chat_id] = []
    active_connections[chat_id].append(websocket)
    try:
        # Invio dei messaggi esistenti al momento della connessione
        db: Session = next(create_session())
        messages = db.query(MesNsage).filter(Message.chat_id == chat_id).all()
        for message in messages:
            await websocket.send_json({"message": message.contenuto, "timestamp": message.timestamp.isoformat()})
        # Gestione dei nuovi messaggi in tempo reale
        while True:
            data = await websocket.receive_text()
            new_message = MessageCreate(chat_id=chat_id, contenuto=data, timestamp=datetime.now())
            db_message = Message(**new_message.dict())
            db.add(db_message)
            db.commit()
            db.refresh(db_message)
            # Invia il nuovo messaggio a tutti i client connessi
            for connection in active_connections[chat_id]:
                await connection.send_json({"message": db_message.contenuto, "timestamp": db_message.timestamp.isoformat()})
    except WebSocketDisconnect:
        active_connections[chat_id].remove(websocket)
        if not active_connections[chat_id]:
            del active_connections[chat_id]
