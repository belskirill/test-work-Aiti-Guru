from src.models.models import OrderItemOrm, OrderOrm, ProductOrm
from src.repository.mappers.base import DataMapper
from src.schema.order import OrderDTO
from src.schema.order_item import OrderItemsDTO
from src.schema.products import ProductDTO


class OrdersDataMapper(DataMapper):
    schema = OrderDTO
    db_model = OrderOrm

class ProductsDataMapper(DataMapper):
    schema = ProductDTO
    db_model = ProductOrm

class OrderItemsDataMapper(DataMapper):
    schema = OrderItemsDTO
    db_model = OrderItemOrm