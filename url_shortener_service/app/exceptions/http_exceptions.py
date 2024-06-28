from http import HTTPStatus

from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class OK200Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.OK, detail=detail)


class Created201Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.CREATED, detail=detail)


class Accepted202Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.ACCEPTED, detail=detail)


class BadRequest400Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.BAD_REQUEST, detail=detail)


class Unauthorized401Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.BAD_REQUEST, detail=detail)


class Forbidden403Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.FORBIDDEN, detail=detail)


class NotFound404Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.NOT_FOUND, detail=detail)


class Conflict409Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTPStatus.CONFLICT, detail=detail)


class InternalServerError500Exception(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=detail
        )
