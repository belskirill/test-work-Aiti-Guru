from src.models.models import OrderOrm
from src.repository.base import BaseRepository
from src.repository.mappers.mappers import OrdersDataMapper


class OrdersRepositories(BaseRepository):
    model = OrderOrm
    mapper = OrdersDataMapper