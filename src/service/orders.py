from src.exceptions.exceptions import OrderNotFoundException, ProductNotFoundException, NotEnoughStockException
from src.schema.order_item import OrderItemCreateDTO
from src.schema.schemas import AddItemRequest
from src.service.base import BaseService


class OrderService(BaseService):

    async def add_order_item(self, data: AddItemRequest):
        order = await self.db.orders.get_one(id=data.order_id)
        if not order:
            raise OrderNotFoundException
        product = await self.db.products.get_one(id=data.product_id)
        if not product:
            raise ProductNotFoundException
        if product.quantity < data.quantity:
            raise NotEnoughStockException

        result = await self.db.order_items.get_one(
            order_id=data.order_id,
            product_id=data.product_id
        )
        if result:
            result.quantity += data.quantity
        else:
            result = await self.db.order_items.add_data(
                OrderItemCreateDTO(order_id=data.order_id, product_id=data.product_id, quantity=data.quantity)
            )
        product.quantity -= data.quantity
        await self.db.commit()
        return result





