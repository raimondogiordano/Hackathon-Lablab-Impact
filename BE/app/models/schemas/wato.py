from pydantic import BaseModel,ConfigDict
from typing import List, Optional
from datetime import date, datetime

import enum

# Enum per lo stato del viaggio
class StatoViaggio(enum.Enum):
    PIANIFICATO = "PIANIFICATO"
    IN_CORSO = "IN_CORSO"
    CONCLUSO = "CONCLUSO"

# Enum per lo stato dell'evento
class StatoEvento(enum.Enum):
    PIANIFICATO = "PIANIFICATO"
    COMPLETATO = "COMPLETATO"
    CANCELLATO = "CANCELLATO"

# Schemas per Utente
class UtenteBase(BaseModel):
    nome: str
    email: str

class UtenteCreate(UtenteBase):
    password: str

class UtenteRead(UtenteBase):
    id: int
    class Config:
        orm_mode = True

# Schemas per Viaggio
class ViaggioBase(BaseModel):
    destinazione: str
    data_partenza: date
    data_arrivo: date
    stato: StatoViaggio|str
    dettagli_biglietto: Optional[str] = None

class ViaggioCreate(ViaggioBase):
    utente_id: int

class ViaggioRead(ViaggioBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    utente_id: int
# Schemas per Itinerario
class ItinerarioBase(BaseModel):
    descrizione: str
    orario: Optional[str] = None

class ItinerarioCreate(ItinerarioBase):
    viaggio_id: int

class ItinerarioRead(ItinerarioBase):
    id: int
    viaggio_id: int
    class Config:
        orm_mode = True

# Schemas per Evento
class EventoBase(BaseModel):
    nome: str
    descrizione: Optional[str] = None
    data_ora: date
    tipo: str
    localizzazione: Optional[str] = None
    stato: StatoEvento

class EventoCreate(EventoBase):
    itinerario_id: int

class EventoRead(EventoBase):
    id: int
    itinerario_id: int
    class Config:
        orm_mode = True

# Schemas per Chat
class ChatBase(BaseModel):
    viaggio_id: int

class ChatCreate(ChatBase):
    pass

class ChatRead(ChatBase):
    id: int
    class Config:
        orm_mode = True

# Schemas per Message
class MessageBase(BaseModel):
    contenuto: str
    timestamp: datetime

class MessageCreate(MessageBase):
    chat_id: int

class MessageRead(MessageBase):
    id: int
    chat_id: int
    class Config:
        orm_mode = True
