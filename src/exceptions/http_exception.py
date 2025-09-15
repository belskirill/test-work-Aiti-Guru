from src.exceptions.base import BaseCustomHTPPException


class ProductNotFoundHTTPException(BaseCustomHTPPException):
    status_code = 404
    detail = "Товар не найден!"


class NotEnoughStockHTTPException(BaseCustomHTPPException):
    status_code = 409
    detail = "Недостаточно товара на складе!"

class OrderNotFoundHTTPException(BaseCustomHTPPException):
    status_code = 404
    detail = "Заказ не найден!"