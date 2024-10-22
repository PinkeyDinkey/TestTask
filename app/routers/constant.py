"""Модуль констант модуля routers"""

from enum import Enum


class RequestType(Enum):
    """Класс перечисления типов запросов"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
