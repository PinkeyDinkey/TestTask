"""
Реализация интерфейса сервиса, предоставляющего основные методы для взаимодействия с объектами типа ссылка
"""


from .url_service import IUrlService
from secrets import token_urlsafe
from validators import url as VUrl

class UrlServiceImplementation(IUrlService):
    """
    Класс реализации интерфейса сервиса, предоставляющий основные методы для взаимодействия с объектами типа
    ссылка
    """

    async def create_short_url(self, url: str) -> str:
        if VUrl(url):
            return await self._url_repository.create_short_url(long_url=url,short_url=token_urlsafe(8))

        return ''

    async def delete_url_by_short_url(self, short_url: str) -> bool:
        return await self._url_repository.delete_url_by_short_url(short_url=short_url)

    async def get_long_url_by_short_url(self, short_url: str) -> str:
        return await self._url_repository.get_long_url_by_short_url(short_url=short_url)
