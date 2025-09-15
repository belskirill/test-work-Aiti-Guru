import logging
from typing import TypeVar, Generic, Type

from asyncpg import UniqueViolationError
from pydantic import BaseModel
from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound, IntegrityError, OperationalError, InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import Base
from src.exceptions.exceptions import DatabaseException, NoResultFoundException
from src.repository.mappers.base import DataMapper


DBModelType = TypeVar("DBModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
MapperType = TypeVar("MapperType", bound=DataMapper)


class BaseRepository(Generic[DBModelType, SchemaType, MapperType]):
    model: Type[DBModelType]
    mapper: Type[MapperType]
    session: AsyncSession

    def __init__(self, session):
        self.session = session

    async def add_data(self, data: BaseModel):
        add_data_stmt = (
            insert(self.model).values(**data.model_dump()).returning(self.model)
        )
        try:
            result = await self.session.execute(add_data_stmt)
            model = result.scalars().one()
            return self.mapper.map_to_domain_entity(model)
        except NoResultFound:
            raise NoResultFoundException
        except IntegrityError as ex:
            logging.error("Ошибка целостности БД", exc_info=True)
            raise DatabaseException("Ошибка целостности данных") from ex

        except (OperationalError, InvalidRequestError) as e:
            logging.error("Ошибка транзакции или соединения с БД", exc_info=True)
            raise DatabaseException("Ошибка работы с базой данных") from e

    async def get_one(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        results = await self.session.execute(query)
        return results.scalars().first()
