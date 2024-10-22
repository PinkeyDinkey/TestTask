"""Модуль инициализации роутеров"""

from fastapi import APIRouter

from .service_routers import service_routers, service_tags_description

routers = APIRouter()
routers.include_router(service_routers)
