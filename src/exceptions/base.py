from fastapi import HTTPException


class BaseCustomHTPPException(HTTPException):
    status_code = 500
    detail = "Неизвестная ошибка"

    def __init__(
        self, detail: str | None = None, status_code: int | None = None
    ):
        super().__init__(
            status_code=status_code or self.status_code,
            detail=detail or self.detail,
        )




class BaseExceptionCustom(Exception):
    detail = "Неизвестная ошибка!!!"

    def __init__(self, detail: str | None = None):

        if detail is None:
            detail = self.detail
        super().__init__(detail)