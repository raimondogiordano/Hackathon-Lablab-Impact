from app.services.base import BaseDataManager
from app.models.data.models import PositionModel
from typing import (
    List
)
from sqlalchemy import select

class PositionDataManager(BaseDataManager):
    def add_entity(self, entity: PositionModel) ->PositionModel:
        """Write user to database."""
        try:
            self.add_one(entity)
            self.session.flush()
            return entity
        except Exception as e:
            print("error saving ",e)
        return entity.to_dict()
    
    def get_by_ai_id(self,ai_id:int)->PositionModel:
        """Get user from database."""
        try:
            stmt=select(PositionModel).where(PositionModel.ai_id==ai_id)
            return self.get_one(stmt)
        except Exception as e:
            print(e)
            raise e
    def get_by_id(self,id:int)->PositionModel:
        """Get user from database."""
        try:
            stmt=select(PositionModel).where(PositionModel.id==id)
            return self.get_one(stmt)
        except Exception as e:
            print(e)
            raise e
