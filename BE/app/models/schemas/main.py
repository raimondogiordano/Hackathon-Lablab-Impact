from pydantic import BaseModel,ConfigDict
from typing import Optional, List


class QuartiereProposal(BaseModel):
    geo_point: Optional[str] = None
    geo_shape: Optional[str] = None
    nome: Optional[str] = None
    quartiere: Optional[str] = None
    zona_prossimita: Optional[str] = None
    proposal: Optional[str] = None
    labels: Optional[List[str]] = None


# Schema for creating a new QuartiereProposal
class QuartiereProposalCreate(BaseModel):
    geo_point: Optional[str] = None
    geo_shape: Optional[str] = None
    nome: Optional[str] = None
    quartiere: Optional[str] = None
    zona_prossimita: Optional[str] = None
    proposal: Optional[str] = None
    labels: Optional[List[str]] = None

# Schema for updating an existing QuartiereProposal
class QuartiereProposalUpdate(BaseModel):
    geo_point: Optional[str] = None
    geo_shape: Optional[str] = None
    nome: Optional[str] = None
    quartiere: Optional[str] = None
    zona_prossimita: Optional[str] = None
    proposal: Optional[str] = None
    labels: Optional[List[str]] = None

# Schema for reading a QuartiereProposal (response model)
class QuartiereProposalRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    geo_point: Optional[str] = None
    geo_shape: Optional[str] = None
    nome: Optional[str] = None
    quartiere: Optional[str] = None
    zona_prossimita: Optional[str] = None
    proposal: Optional[str] = None
    labels: Optional[List[str]] = None


# Schema for listing multiple QuartiereProposals
class QuartiereProposalList(BaseModel):
    proposals: List[QuartiereProposalRead]

# Schema for deleting a QuartiereProposal
class QuartiereProposalDelete(BaseModel):
    id: int
