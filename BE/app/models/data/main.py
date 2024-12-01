from sqlalchemy import String, Text, Integer, ARRAY
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class QuartiereProposalModel(Base):
    __tablename__ = 'quartiere_proposal'

    id = mapped_column(Integer, primary_key=True, index=True)
    geo_point = mapped_column(String, nullable=True)
    geo_shape = mapped_column(Text, nullable=True)
    nome = mapped_column(String, nullable=True)
    quartiere = mapped_column(String, nullable=True)
    zona_prossimita = mapped_column(String, nullable=True)
    proposal = mapped_column(Text, nullable=True)
    labels = mapped_column(ARRAY(String), nullable=True)
