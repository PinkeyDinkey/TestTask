"""Модуль конфигурации зависимостей модулей"""

from inject import Binder

from app.modules.url_reduction import inject_config_url


def config(binder: Binder) -> None:
    """
    Метод конфигурации зависимостей модулей

    Args:
        binder (Binder): Объект Binder

    Returns:
        None
    """
    binder.install(inject_config_url)
