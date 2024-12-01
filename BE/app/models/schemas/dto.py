from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Posizione (Ruolo per cui ci si candida)
class PositionFilter(BaseModel):
    id: int
    ai_id: int
    title: str
    description: str
    requirements: str
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

class UpdateCvByName(BaseModel):
    name:str
    update_params:dict

class UpdateParamsEvaluation(BaseModel):
    curriculum_name:str
    weakness:str
    summary:str
    strength:str
    score:float|str
     
class UpdateEvaluationByCvByPosition(BaseModel):
    ai_id: int
    update_params:List[UpdateParamsEvaluation]
    
