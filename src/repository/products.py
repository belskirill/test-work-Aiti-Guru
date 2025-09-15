from src.models.models import ProductOrm
from src.repository.base import BaseRepository
from src.repository.mappers.mappers import ProductsDataMapper


class ProductsRepositories(BaseRepository):
    model = ProductOrm
    mapper = ProductsDataMapper