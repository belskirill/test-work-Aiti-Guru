import logging

from fastapi import APIRouter

from src.exceptions.base import BaseCustomHTPPException
from src.exceptions.exceptions import NotEnoughStockException, ProductNotFoundException, OrderNotFoundException
from src.exceptions.http_exception import ProductNotFoundHTTPException, NotEnoughStockHTTPException, \
    OrderNotFoundHTTPException
from src.schema.schemas import AddItemRequest
from src.api.dependencies import DBDep
from src.service.orders import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/add-item")
async def add_item(
    data: AddItemRequest,
    db: DBDep
):
    try:
        return await OrderService(db).add_order_item(data)
    except OrderNotFoundException:
        raise OrderNotFoundHTTPException()
    except ProductNotFoundException:
        raise ProductNotFoundHTTPException()
    except NotEnoughStockException:
        raise NotEnoughStockHTTPException()
    except Exception as e:
        logging.critical(e, exc_info=True)
        raise BaseCustomHTPPException()
