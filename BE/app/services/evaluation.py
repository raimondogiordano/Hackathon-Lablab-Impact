from app.services.base import BaseDataManager
from app.models.data.models import EvaluationModel
from typing import (
    List
)
from sqlalchemy import select

class EvaluationDataManager(BaseDataManager):
    def add_entity(self, entity: EvaluationModel) ->EvaluationModel:
        """Write cv to database."""
        try:
            self.add_one(entity)
            self.session.flush()
            return entity
        except Exception as e:
            print("error saving ",e)
        return entity.to_dict()

    def list_all(self) ->List[EvaluationModel]:
        """List all cvs."""
        try:
            stmt=select(EvaluationModel).where(EvaluationModel.id>0)
            return self.get_all(stmt)
        except Exception as e:
            print(e)
            raise e
    def update_by_position_and_cv(self, position_id: int,curriculum_id:int, update_params: dict) -> None:
        """
        Update a Evaluation entity for a match between CV and Position using the provided update parameters.
        """
        try:
            filter = {'positionId': position_id,"curriculumId":curriculum_id}
            self.update(EvaluationModel, filter, update_params)
        except Exception as e:
            print(e)
            raise e
    def get_by_cv(self, curriculum_id: int) -> List[EvaluationModel]:
        """Get all evaluations for a specific CV."""
        try:
            stmt = select(EvaluationModel).where(EvaluationModel.curriculumId == curriculum_id)
            return self.get_all(stmt)
        except Exception as e:
            print(e)
            raise e