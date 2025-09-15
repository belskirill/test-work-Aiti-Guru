from src.models.models import OrderItemOrm
from src.repository.base import BaseRepository
from src.repository.mappers.mappers import OrderItemsDataMapper


class OrdersItemsRepositories(BaseRepository):
    model = OrderItemOrm
    mapper = OrderItemsDataMapper