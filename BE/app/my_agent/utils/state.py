from typing import TypedDict, Optional


# Definiamo lo stato dell'agente
class AgentState(TypedDict):
    nome_proposta: Optional[str]
    quartiere: Optional[str]
    zona_prossimita: Optional[str]
    proposal: Optional[str]
    labels: Optional[list[str]] = None
    messages: list[dict]