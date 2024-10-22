"""
Интерфейс сервиса, предоставляющий основные методы для взаимодействия с объектами типа ссылка
"""

from abc import ABC, abstractmethod

from inject import attr

from .url_repository import IUrlRepository


class IUrlService(ABC):
    """
    Класс интерфейса сервиса, предоставляющий основные методы для взаимодействия с объектами типа ссылка
    """

    _url_repository: IUrlRepository = attr(IUrlRepository)

    @abstractmethod
    async def create_short_url(self, url: str) -> str:
        """
        Метод создания информации о ссылке

        Args:
            url (str): Полная ссылка


        Returns:
            str: Сокращенная ссылка
        """

    @abstractmethod
    async def delete_url_by_short_url(self, short_url: str) -> bool:
        """
        Метод удаления информации о ссылке по сокращенной ссылке

        Args:
            short_url (str): Сокращенная ссылка

        Returns:
            bool: Булевый результат удаления
        """

    @abstractmethod
    async def get_long_url_by_short_url(self, short_url: str) -> str:
        """
        Метод получения полной ссылки по сокращенной ссылке

        Args:
            short_url (str): Сокращенная ссылка

        Returns:
            str: Полная ссылка
        """

