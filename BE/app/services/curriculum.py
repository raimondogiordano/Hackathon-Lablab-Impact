from app.services.base import BaseDataManager
from app.models.data.models import CurriculumModel
from typing import (
    List
)
from sqlalchemy import select

class CurriculumDataManager(BaseDataManager):
    def add_entity(self, entity: CurriculumModel) ->CurriculumModel:
        """Write cv to database."""
        try:
            self.add_one(entity)
            self.session.flush()
            return entity
        except Exception as e:
            print("error saving ",e)
        return entity.to_dict()
    def add_entities(self, entities: List[CurriculumModel]) ->List[CurriculumModel]:
        """Write cv to database."""
        try:
            self.add_entities(entities)
            self.session.flush()
            return entities
        except Exception as e:
            print("error saving ",e)
        return entity.to_dictstr
    def get_one_by_name(self, name: int) -> CurriculumModel:
        """Retrieve a single cv by its name."""
        try:
            stmt = select(CurriculumModel).where(CurriculumModel.name == name)
            result = self.session.execute(stmt).scalar()
            return result
        except Exception as e:
            print(f"Error retrieving entity with id {id}: ", e)
            raise e
    def list_all(self) ->List[CurriculumModel]:
        """List all cvs."""
        try:
            stmt=select(CurriculumModel).where(CurriculumModel.id>0)
            return self.get_all(stmt)
        except Exception as e:
            print(e)
            raise e
    def update_by_name(self, name: str, update_params: dict) -> None:
        """
        Update a CurriculumModel entity by its name using the provided update parameters.
        """
        try:
            filter = {'name': name}
            self.update(CurriculumModel, filter, update_params)
        except Exception as e:
            print(e)
            raise e
    def delete_by_name(self, name: str) -> None:
        """
        Delete a CurriculumModel entity by its name.
        """
        try:
            filter = {'name': name}
            self.delete(CurriculumModel, filter)
        except Exception as e:
            print(e)
            raise e