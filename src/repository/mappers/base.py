from typing import TypeVar, Type, Generic, Union
from pydantic import BaseModel
from sqlalchemy import Row, RowMapping
from src.core.database import Base

SchemaType = TypeVar("SchemaType", bound=BaseModel)
DBModelType = TypeVar("DBModelType", bound=Base)


class DataMapper(Generic[DBModelType, SchemaType]):
    db_model: Type[DBModelType]
    schema: Type[SchemaType]

    @classmethod
    def map_to_domain_entity(
        cls, data: Union[DBModelType, dict, Row, RowMapping]
    ) -> SchemaType:
        return cls.schema.model_validate(data, from_attributes=True)

    @classmethod
    def map_to_persistence_entity(cls, data: SchemaType) -> DBModelType:
        return cls.db_model(**data.model_dump())
