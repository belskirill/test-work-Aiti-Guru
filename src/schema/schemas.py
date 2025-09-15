from pydantic import BaseModel, ConfigDict, conint


class AddItemRequest(BaseModel):
    order_id: int
    product_id: int
    quantity: conint(gt=0)

class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)
