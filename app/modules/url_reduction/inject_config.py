"""Конфигурация зависимостей модуля url_reduction"""

from inject import Binder

from .domain import IUrlRepository, IUrlService, UrlServiceImplementation
from .infrastructure import SQLAlchemyUrlRepository


def inject_config_url(binder: Binder) -> None:
    """
    Метод конфигурации зависимостей модуля url_reduction

    Args:
        binder (Binder): Объект Binder

    Returns:
        None
    """

    # url region
    binder.bind(IUrlService, UrlServiceImplementation())
    binder.bind(IUrlRepository, SQLAlchemyUrlRepository())
    # end region
