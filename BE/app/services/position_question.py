from app.services.base import BaseDataManager
from app.models.data.models import PositionQuestionModel
from typing import List
from sqlalchemy import select

class PositionQuestionDataManager(BaseDataManager):
    def add_entity(self, entity: PositionQuestionModel) -> PositionQuestionModel:
        """Add a single position question to the database."""
        try:
            self.add_one(entity)
            self.session.flush()
            return entity
        except Exception as e:
            print("error saving ", e)
        return entity.to_dict()

    def add_entities(self, entities: List[PositionQuestionModel]) -> List[PositionQuestionModel]:
        """Add multiple position questions to the database."""
        try:
            self.add_many(entities)
            self.session.flush()
            return entities
        except Exception as e:
            print("error saving ", e)
        return [entity.to_dict() for entity in entities]

    def get_one_by_id(self, id: int) -> PositionQuestionModel:
        """Retrieve a single position question by its ID."""
        try:
            stmt = select(PositionQuestionModel).where(PositionQuestionModel.id == id)
            result = self.session.execute(stmt).scalar()
            return result
        except Exception as e:
            print(f"Error retrieving entity with id {id}: ", e)
            raise e
    def get_one_by_position(self, position_id: int) -> PositionQuestionModel:
        """Retrieve a single position question by its ID."""
        try:
            stmt = select(PositionQuestionModel).where(PositionQuestionModel.positionId == position_id).order_by(PositionQuestionModel.item_order)
            result = self.get_all(stmt)
            return result
        except Exception as e:
            print(f"Error retrieving entity with id {id}: ", e)
            raise e

    def list_all(self) -> List[PositionQuestionModel]:
        """List all position questions."""
        try:
            stmt = select(PositionQuestionModel).order_by(PositionQuestionModel.item_order)
            return self.get_all(stmt)
        except Exception as e:
            print(e)
            raise e

    def update_by_id(self, id: int, update_params: dict) -> None:
        """
        Update a PositionQuestionModel entity by its ID using the provided update parameters.
        """
        try:
            filter = {'id': id}
            self.update(PositionQuestionModel, filter, update_params)
        except Exception as e:
            print(e)
            raise e
    def delete_by_id(self, id: int) -> None:
        """
        Delete a PositionQuestionModel entity by its ID.
        """
        try:
            self.delete(PositionQuestionModel, {'id': id})
        except Exception as e:
            print(e)
            raise e