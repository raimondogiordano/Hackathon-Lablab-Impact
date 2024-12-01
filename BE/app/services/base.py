from typing import (
    Any,
    List,
    Sequence,
    Type,
    Dict
)

from sqlalchemy import (
    func,
    select,
    update,
    delete,
    desc, asc
)
from sqlalchemy.orm import (
    Session
)
from sqlalchemy.sql.expression import Executable
from app.models.data.base import SQLModel


class SessionMixin:
    """Provides instance of database session."""

    def __init__(self, session: Session) -> None:
        self.session = session





class BaseDataManager(SessionMixin):
    """Base data manager class responsible for operations over database."""

    def add_one(self, model: Any) -> None:
        self.session.add(model)

    def add_all(self, models: Sequence[Any]) -> None:
        self.session.add_all(models)

    def update(self, model: Any, filter: Any, params: List[Any]) -> None:
        query = self.session.query(model)
        for attr,value in filter.items():
            if value is not None:
                query = query.filter( getattr(model, attr)==value )
        query.update(params)

    def delete(self, model: Any, filter: Any) -> None:
        query = self.session.query(model)
        for attr,value in filter.items():
            if value is not None:
                query = query.filter( getattr(model, attr)==value )
        query.delete()

    def get_one(self, select_stmt: Executable) -> Any:
        return self.session.scalar(select_stmt)

    def get_all_by_filter(self, model: Any, filter: Dict) -> List[Any]:
        query = self.session.query(model)
        for attr,value in filter.items():
            if value is not None:
                query = query.filter( getattr(model, attr)==value )
        return query.all()

    def get_all_by_filter_and_order(self, model: Any, filter: Dict, order: Dict) -> List[Any]:
        query = self.session.query(model)
        for attr,value in filter.items():
            if value is not None:
                query = query.filter( getattr(model, attr)==value )
        for attr in order:
            if order[attr] == 'asc':
                query = query.order_by( asc(getattr(model, attr)) )
            else:
                query = query.order_by( desc(getattr(model, attr)) )
        return query.all()

    def get_all_by_filter_and_order_and_paging(self, model: Any, filter: Dict, order: Dict, page=0, page_size=None) -> List[Any]:
        query = self.session.query(model)
        for attr,value in filter.items():
            if value is not None:
                query = query.filter( getattr(model, attr)==value )
        for attr in order:
            if order[attr] == 'asc':
                query = query.order_by( asc(getattr(model, attr)) )
            else:
                query = query.order_by( desc(getattr(model, attr)) )
        if page_size:
            query = query.limit(page_size)
        if page: 
            query = query.offset(page*page_size)
        return query.all()

    def get_all(self, select_stmt: Executable) -> List[Any]:
        return list(self.session.scalars(select_stmt).all())

    def get_from_tvf(self, model: Type[SQLModel], *args: Any) -> List[Any]:
        """Query from table valued function.

        This is a wrapper function that can be used to retrieve data from
        table valued functions.

        Examples:
            from app.models.base import SQLModel

            class MyModel(SQLModel):
                __tablename__ = "function"
                __table_args__ = {"schema": "schema"}

                x: Mapped[int] = mapped_column("x", primary_key=True)
                y: Mapped[str] = mapped_column("y")
                z: Mapped[float] = mapped_column("z")

            # equivalent to "SELECT x, y, z FROM schema.function(1, "AAA")"
            BaseDataManager(session).get_from_tvf(MyModel, 1, "AAA")
        """

        fn = getattr(getattr(func, model.schema()), model.table_name())
        stmt = select(fn(*args).table_valued(*model.fields()))
        return self.get_all(select(model).from_statement(stmt))

    def count_all_by_filter(self, model: Any, filter: Dict) -> Any:
        query = self.session.query(model)
        for attr,value in filter.items():
            if value is not None:
                query = query.filter( getattr(model, attr)==value )
        #return query.with_entities(func.count()).scalar()
        return query.count()

    def sum_all_by_filter(self, model: Any, filter: Dict, field: Any) -> Any:
        query = self.session.query(model)
        for attr,value in filter.items():
            if value is not None:
                query = query.filter( getattr(model, attr)==value )
        return query.with_entities(func.sum(field)).scalar()

class BaseService(SessionMixin):
    """Base class for application services."""
    model=BaseDataManager()