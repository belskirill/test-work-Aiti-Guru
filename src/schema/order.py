from datetime import datetime

from pydantic import BaseModel


class OrderDTO(BaseModel):
    id: int
    client_id: int
    created_at: datetime