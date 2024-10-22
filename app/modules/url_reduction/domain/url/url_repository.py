"""
Интерфейс репозитория, предоставляющий основные методы для взаимодействия с объектами типа ссылка
"""

from abc import ABC, abstractmethod


class IUrlRepository(ABC):
    """
    Класс репозитория, предоставляющий основные методы для взаимодействия с объектами типа ссылка
    """

    @abstractmethod
    async def create_short_url(self, long_url: str, short_url: str) -> str:
        """
        Метод создания информации о ссылке

        Args:
            long_url (str): Полная ссылка
            short_url (str): Сокращенная ссылка

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
