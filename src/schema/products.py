from pydantic import BaseModel


class ProductDTO(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
    category_id: int