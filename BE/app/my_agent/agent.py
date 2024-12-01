from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from app.my_agent.utils.state import AgentState
from app.my_agent.utils.tools import tools
from app.my_agent.groq import initialize_agent_groq
from pydantic import BaseModel,ValidationError
from app.my_agent.groq_v2 import GroqLlama


llm=GroqLlama()

class Proposta(BaseModel):
    nome_proposta: str
    quartiere: str
    zona_prossimita: str
    proposal: str
    labels: list[str]
    messages: list[dict]
    
def collect_information(state, config):
    messages = state.get("messages", [])
    if not state.get("nome_proposta"):
        prompt = llm(task_type="completion",completion_prompt="Chiedi all'utente il nome della proposta")
    elif not state.get("quartiere"):
        prompt = llm(task_type="completion",completion_prompt="Chiedi all'utente il nome del quartiere a cui la proposta si riferisce")
    elif not state.get("proposal"):
        prompt = llm(task_type="completion",completion_prompt="Chiedi all'utente informazioni sulla proposta")
    else:
        return state  # Tutte le informazioni sono state raccolte

    # Aggiungiamo il messaggio al contesto
    messages.append({"role": "system", "content": prompt})
    state["messages"] = messages
    return state
def verify_place(state, config):
    return state
def verify(state, config):
    try:
        # Creare un'istanza di Proposta passando lo stato come keyword arguments
        proposta = Proposta(**state)  # Questo convaliderà i dati all'istante
        return "classify_proposal"
    except ValidationError as e:
        # Stampa l'errore per aiutare nel debug
        print(f"Errore di validazione: {e}")
        return "collect_information"

# Nodo per classificare automaticamente le etichette in base alla proposta
def classify_proposal(state, config):
    if not state.get("labels") and state.get("proposal"):
        state["labels"] = llm(task_type="completion",completion_prompt="Date queste labels ['Inclusione Sociale','Supporto ai Bambini','Spazi Verdi','Sicurezza','Pulizia Urbana','Coesione Sociale','Rigenerazione Urbana','Prossimità ai Servizi','Promozione Culturale','Iniziative Sociali','Sostenibilità Climatica','Conoscenza e Informazione'] attribuisci tutte le labels che ritieni opportune alla proposta seguente "+state["proposal"])
    return state

# Nodo per trovare la zona di prossimità usando il web
def find_zone(state, config):
    if not state.get("zona_prossimita") and state.get("quartiere"):
        state["zona_prossimita"] = llm(task_type="completion",completion_prompt="Dato un quartiere di Bologna cerca su internet il singolo quartiere più vicino e restituisci solo il nome del quartiere trovato. NOME QUARTIERE:")
    return state


class ProposalCatcherAgent():
    def __init__(self):
        
        workflow = StateGraph(AgentState)

        workflow.add_node("collect_information", collect_information)
        workflow.add_node("verify_info", verify_place)
        workflow.add_node("classify_proposal", classify_proposal)
        workflow.add_node("find_zone", find_zone)

        # Definiamo l'entry point del workflow
        workflow.set_entry_point("collect_information")

        # Definiamo le edge del grafo
        workflow.add_edge("collect_information","verify_info")
        workflow.add_conditional_edges("verify_info", verify, {"classify_proposal": "classify_proposal", "collect_information": END})
        workflow.add_edge("classify_proposal", "find_zone")
        workflow.add_edge("find_zone", END)

        self.graph = workflow.compile()
