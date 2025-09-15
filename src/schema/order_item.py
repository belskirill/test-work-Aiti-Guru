from pydantic import BaseModel


class OrderItemsDTO(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int


class OrderItemCreateDTO(BaseModel):
    order_id: int
    product_id: int
    quantity: int