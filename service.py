"""Модуль метода инициализации объекта приложения для его дальнейшего запуска на ASGI"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import configure_app
from app.routers import routers
from constant import DOCS_PATH, SERVICE_TITLE, VERSION


@asynccontextmanager
async def lifespan(application: FastAPI):
    """
    Метод обработки события начала и окончания работы сервиса

    Args:
        application (FastAPI): Объект приложения FastAPI

    Returns:
        None
    """
    # Действие сразу после запуска
    await configure_app()
    yield
    # Действие сразу после завершения


def create_app() -> FastAPI:
    """
    Метод создания объекта приложения FastAPI

    Returns:
        FastAPI: Объект приложения FastAPI
    """
    new_app = FastAPI(lifespan=lifespan, title=SERVICE_TITLE, version=VERSION, docs_url=DOCS_PATH)

    # Инициализация промежуточных слоев
    new_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["POST"],
        allow_headers=["*"],
    )

    # Инициализация эндпоинтов сервиса
    new_app.include_router(routers)

    return new_app
