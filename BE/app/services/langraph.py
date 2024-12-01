from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from my_agent.utils.nodes import classify_labels, find_proximity_zone
from my_agent.utils.state import AgentState
from my_agent.utils.tools import tools

class GraphConfig(TypedDict):
    model_name: Optional[str] = "openai"

# Definiamo lo stato dell'agente
class AgentState(TypedDict):
    nome_proposta: Optional[str]
    quartiere: Optional[str]
    zona_prossimita: Optional[str]
    proposal: Optional[str]
    labels: Optional[list[str]] = None
    messages: list[dict]

# Creiamo un grafo per il workflow
workflow = StateGraph(AgentState, config_schema=GraphConfig)

# Nodo per iniziare il dialogo con l'utente in modo naturale
def collect_information(state, config):
    messages = state.get("messages", [])
    if not state.get("nome_proposta"):
        prompt = "Ciao! Mi piacerebbe sapere il nome della tua proposta, così possiamo iniziare a discutere di un'idea interessante per il quartiere."
    elif not state.get("quartiere"):
        prompt = f"Perfetto, ottimo nome {state['nome_proposta']}! In quale quartiere vorresti proporre un'idea?"
    elif not state.get("proposal"):
        prompt = "Ottimo! Raccontami della tua proposta. Che tipo di iniziativa hai in mente per migliorare il quartiere?"
    else:
        return state  # Tutte le informazioni sono state raccolte

    # Aggiungiamo il messaggio al contesto
    messages.append({"role": "system", "content": prompt})
    state["messages"] = messages
    return state

# Nodo per classificare automaticamente le etichette in base alla proposta
def classify_proposal(state, config):
    if not state.get("labels") and state.get("proposal"):
        state["labels"] = classify_labels(state["proposal"])
    return state

# Nodo per trovare la zona di prossimità usando il web
def find_zone(state, config):
    if not state.get("zona_prossimita") and state.get("quartiere"):
        state["zona_prossimita"] = find_proximity_zone(state["quartiere"])
    return state

# Aggiungiamo i nodi al workflow
workflow.add_node("collect_information", collect_information)
workflow.add_node("classify_proposal", classify_proposal)
workflow.add_node("find_zone", find_zone)

# Definiamo l'entry point del workflow
workflow.set_entry_point("collect_information")

# Definiamo le edge del grafo
workflow.add_edge("collect_information", "classify_proposal")
workflow.add_edge("classify_proposal", "find_zone")
workflow.add_edge("find_zone", END)

# Compiliamo il workflow in un oggetto eseguibile
agent_graph = workflow.compile()
