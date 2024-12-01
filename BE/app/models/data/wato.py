# from sqlalchemy import String, Integer, ForeignKey, Date, Enum
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import mapped_column
# import enum
# from app.models.data.base import SQLModel
# from pydantic import BaseModel
# from typing import List, Optional

# # Enum per lo stato del viaggio
# class StatoViaggio(enum.Enum):
#     PIANIFICATO = "PIANIFICATO"
#     IN_CORSO = "IN_CORSO"
#     CONCLUSO = "CONCLUSO"

# # Modello Utente
# class Utente(SQLModel):
#     __tablename__ = 'utenti'
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     nome = mapped_column(String, nullable=False)
#     email = mapped_column(String, unique=True, nullable=False)
#     password_hash = mapped_column(String, nullable=False)
    
#     viaggi = relationship("Viaggio", back_populates="utente")

# # Modello Viaggio
# class Viaggio(SQLModel):
#     __tablename__ = 'viaggi'
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     utente_id = mapped_column(Integer, ForeignKey('utenti.id'), nullable=False)
#     destinazione = mapped_column(String, nullable=False)
#     data_arrivo = mapped_column(Date, nullable=False)
#     data_partenza = mapped_column(Date, nullable=False)
#     stato = mapped_column(Enum(StatoViaggio), default=StatoViaggio.PIANIFICATO, nullable=False)
#     dettagli_biglietto = mapped_column(String, nullable=True)  # Informazioni sui biglietti
    
#     utente = relationship("Utente", back_populates="viaggi")
#     itinerari = relationship("Itinerario", back_populates="viaggio")
#     chat = relationship("Chat", back_populates="viaggio", uselist=False)

# # Modello Itinerario
# class Itinerario(SQLModel):
#     __tablename__ = 'itinerari'
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     viaggio_id = mapped_column(Integer, ForeignKey('viaggi.id'), nullable=False)
#     descrizione = mapped_column(String, nullable=False)
#     orario = mapped_column(String, nullable=True)  # Orario dell'attività
#     viaggio = relationship("Viaggio", back_populates="itinerari")
#     eventi = relationship("Evento", back_populates="itinerario")
# class Evento(SQLModel):
#     __tablename__ = 'evento'

#     id = mapped_column(Integer, primary_key=True, index=True)
#     itinerario_id = mapped_column(Integer, ForeignKey('itinerari.id'), nullable=False)
#     nome = mapped_column(String, nullable=False)
#     descrizione = mapped_column(String, nullable=True)
#     data_ora = mapped_column(Date, nullable=False)
#     tipo = mapped_column(String, nullable=False)  # Potresti definire un enum per il tipo di evento
#     localizzazione = mapped_column(String, nullable=True)
#     stato = mapped_column(String, default="pianificato", nullable=False)  # Potresti usare un enum (es. pianificato, completato, cancellato)

#     itinerario = relationship("Itinerario", back_populates="eventi")
# # Modello Chat
# class Chat(SQLModel):
#     __tablename__ = 'chats'
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     viaggio_id = mapped_column(Integer, ForeignKey('viaggi.id'), nullable=False)
    
#     viaggio = relationship("Viaggio", back_populates="chat")
#     messaggi = relationship("Message", back_populates="chat")

# # Modello Message
# class Message(SQLModel):
#     __tablename__ = 'messages'
    
#     id = mapped_column(Integer, primary_key=True, index=True)
#     chat_id = mapped_column(Integer, ForeignKey('chats.id'), nullable=False)
#     contenuto = mapped_column(String, nullable=False)
#     timestamp = mapped_column(Date, nullable=False)  # Timestamp del messaggio
    
#     chat = relationship("Chat", back_populates="messaggi")
