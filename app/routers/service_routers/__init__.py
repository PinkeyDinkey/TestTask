"""Модуль импортов и инициализации системных эндпоинтов"""

from fastapi import APIRouter

from .routers_url_reduce import UrlReduceRouters

service_tags_description = [
    {"name": "url_reduce", "description": "Запросы для работы с сокращением ссылок"},
]

service_routers = APIRouter()
service_routers.include_router(UrlReduceRouters().router, tags=["url_reduce"])
