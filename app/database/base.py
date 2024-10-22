"""Модуль настроек sqlalchemy (подключение, конфигурация метадаты, настройка движка и т.п.)"""

from asyncio import current_task
from typing import Any

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.declarative import declarative_base

from settings import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{settings.db_username}:"
    f"{settings.db_password}@{settings.db_host}:"
    f"{settings.db_port}/{settings.db_name}"
)

engine = create_async_engine(url=SQLALCHEMY_DATABASE_URL, echo=True)
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()

AsyncScopedSession = async_scoped_session(session_factory=async_session, scopefunc=current_task)


def get_async_scoped_session() -> async_scoped_session[AsyncSession | Any]:
    """
    Метод получения асинхронной скоуп сессии

    Returns:
        async_scoped_session[AsyncSession | Any]: Асинхронная скоуп сессия
    """
    return AsyncScopedSession
