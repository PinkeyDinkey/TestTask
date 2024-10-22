"""Модуль описания роутеров для работы с объектом типа работник"""

from fastapi import APIRouter, Response, status
from inject import attr
from pydantic import BaseModel, Field
from starlette.responses import RedirectResponse

from app.database.base import AsyncScopedSession
from app.database.transaction_factory import TransactionFactory
from app.modules.url_reduction.domain.url import IUrlService
from app.routers.constant import RequestType
from .constant import (
    CREATE_REDUCED_URL_DESC,
    CREATE_REDUCED_URL_PATH,
    DELETE_REDUCED_URL_DESC,
    DELETE_REDUCED_URL_PATH,
    GET_FULL_BY_REDUCED_URL_DESC,
    GET_FULL_BY_REDUCED_URL_PATH,
)


class Url(BaseModel):
    url: str = Field(
        pattern=r'^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$'
    )


class ShortUrl(BaseModel):
    short_url: str = Field(min_length=5, max_length=16)


class UrlReduceRouters:
    """Класс описания роутеров для работы с объектом типа работник"""

    _url_service: IUrlService = attr(IUrlService)
    _router = None

    def __init__(self):
        self._session = AsyncScopedSession

        self.router = APIRouter()

        self.router.add_api_route(
            path=CREATE_REDUCED_URL_PATH,
            endpoint=self.create_reduced_url,
            methods=[RequestType.POST.name],
            status_code=status.HTTP_201_CREATED,
        )
        self.router.add_api_route(
            path=GET_FULL_BY_REDUCED_URL_PATH,
            endpoint=self.get_full_by_reduced_url,
            methods=[RequestType.GET.name],
        )
        self.router.add_api_route(
            path=DELETE_REDUCED_URL_PATH,
            endpoint=self.delete_reduced_url,
            methods=[RequestType.DELETE.name],
            status_code=status.HTTP_204_NO_CONTENT,
        )

    async def create_reduced_url(self, url: Url) -> str:
        """
        Эндпоинт создания сокращенной ссылки

        Args:
            url (Url): Объект обмена данными о создании сокращенной ссылки

        Returns:
            str: Сокращенная ссылка
        """
        async with TransactionFactory(session=self._session).get_transaction():
            result = await self._url_service.create_short_url(url=url.url)

        return result

    async def delete_reduced_url(self, short_url: ShortUrl, responce: Response) -> None:
        """
        Эндпоинт удаления сокращенной ссылки

        Args:
            short_url (ShortUrl): Объект обмена данными об удалении сокращенной ссылки
            responce (Response): Объект ответа сервера

        Returns:
            None
        """
        async with TransactionFactory(session=self._session).get_transaction():
            if await self._url_service.delete_url_by_short_url(short_url=short_url.short_url):
                responce.status_code = status.HTTP_204_NO_CONTENT
            else:
                responce.status_code = status.HTTP_409_CONFLICT

    async def get_full_by_reduced_url(self, short_url: str, responce: Response) -> RedirectResponse:
        """
        Эндпоинт редиректа по сокращенной ссылке

        Args:
            short_url (str): Идентификатор сокращенной ссылки
            responce (Response): Объект ответа сервера

        Returns:
            RedirectResponse: Объект переадресации
        """
        async with TransactionFactory(session=self._session).get_transaction():
            if result := await self._url_service.get_long_url_by_short_url(short_url=short_url):
                return RedirectResponse(url=result)

            responce.status_code = status.HTTP_404_NOT_FOUND
