from src.exceptions.base import BaseExceptionCustom


class ProductNotFoundException(BaseExceptionCustom):
    detail = "Товар не найден!"


class NotEnoughStockException(BaseExceptionCustom):
    detail = "Недостаточно товара на складе!"


class OrderNotFoundException(BaseExceptionCustom):
    detail = "Заказ не найден!"

class DatabaseException(BaseExceptionCustom):
    detail = "Ошибка целостности БД!"

class NoResultFoundException(BaseExceptionCustom):
    detail = "Объект не найден!"