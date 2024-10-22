"""Модуль конфигурации зависимостей"""

from inject import configure

from .inject_config import config


async def configure_app() -> None:
    """
    Метод конфигурации зависимостей

    Returns:
        None
    """
    configure(config)
