"""
Реализация интерфейса репозитория для взаимодействия с объектами типа ссылка средствами SQLAlchemy
"""

from sqlalchemy import delete, select

from app.database.base import AsyncScopedSession
from app.database.transaction_factory import TransactionFactory
from app.modules.url_reduction.domain.url import IUrlRepository
from app.modules.url_reduction.infrastructure.sa_orm import Url as ORMUrl
from .constant import EMPTY_URL


class SQLAlchemyUrlRepository(IUrlRepository):
    """
    Класс реализации интерфейса репозитория для взаимодействия с объектами типа ссылка средствами SQLAlchemy
    """

    def __init__(self):
        self._session = AsyncScopedSession

    async def create_short_url(self, long_url: str, short_url: str) -> str:
        async with TransactionFactory(session=self._session).get_transaction():
            current_session = self._session()

            url = ORMUrl(long_url=long_url, short_url=short_url)
            current_session.add(url)

            await current_session.flush()

        return url.short_url if url else EMPTY_URL

    async def delete_url_by_short_url(self, short_url: str) -> bool:
        async with TransactionFactory(session=self._session).get_transaction():
            current_session = self._session()

            query = delete(ORMUrl).filter(ORMUrl.short_url == short_url).returning(ORMUrl)

            result = await current_session.execute(query)

        return bool(result.fetchall())

    async def get_long_url_by_short_url(self, short_url: str) -> str:
        async with TransactionFactory(session=self._session).get_transaction():
            current_session = self._session()

            query = select(ORMUrl).filter(ORMUrl.short_url == short_url)

            result = (await current_session.execute(query)).scalar()

        return result.long_url if result else EMPTY_URL
