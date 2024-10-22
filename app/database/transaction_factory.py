"""Модуль описания фабрики транзакций"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_scoped_session


class TransactionFactory:
    """Класс фабрики транзакции"""

    def __init__(self, session: async_scoped_session):
        self._session = session

    @asynccontextmanager
    async def get_transaction(self) -> AsyncGenerator:
        """
        Метод-генератор получения транзакции

        ВАЖНО! Если используется менеджер транзакций необходимо следить за ивент лупом, чтобы внутри
        транзакций он был единственным. Например, вызов gather внутри транзакции приведет к неожиданному
        результату

        Returns:
            AsyncGenerator: Асинхронный генератор транзакции
        """
        session = self._session()
        rollback_flag = False
        init_transaction = False

        if session.in_transaction():
            transaction = session.get_transaction()
        else:
            transaction = session.begin()
            init_transaction = True
            await transaction.start()

        try:
            yield transaction
        except Exception as error:  # pylint: disable=broad-exception-caught
            if init_transaction:
                rollback_flag = True
            raise error from error
        finally:
            if init_transaction:
                if rollback_flag:
                    await transaction.rollback()
                else:
                    await transaction.commit()

                await session.close()
                await self._session.remove()
