from typing import Any, Iterable, Mapping
from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row

from app.interfaces.sql import DatabaseInterface
from app.settings.config import settings


class AdapterPostgres(DatabaseInterface):
    """
    PostgreSQL adapter using psycopg3 AsyncConnectionPool.

    The pool is created once and kept open for the entire
    application lifecycle.
    """

    def __init__(self, **kwargs: Any) -> None:
        conninfo = (
            f"postgresql://{settings.PSQL_USERNAME_MEMORY}:"
            f"{settings.PSQL_PASSWORD_MEMORY}@"
            f"{settings.PSQL_HOST_MEMORY}:"
            f"{settings.PSQL_PORT_MEMORY}/"
            f"{settings.PSQL_DATABASE_MEMORY}"
            f"?sslmode={settings.PSQL_SSLMODE_MEMORY or ''}"
        )

        self.__pool = AsyncConnectionPool(
            conninfo=conninfo,
            max_size=20,
            kwargs={
                "autocommit": True,
                "prepare_threshold": 0,
                "row_factory": dict_row,
            },
        )

    async def execute(
        self,
        query: str,
        params: Mapping[str, Any] | None = None,
    ) -> None:
        async with self.__pool.connection() as conn:
            await conn.execute(query, params)

    async def fetch_one(
        self,
        query: str,
        params: Mapping[str, Any] | None = None,
    ) -> Mapping[str, Any] | None:
        async with self.__pool.connection() as conn:
            row = await conn.execute(query, params)
            result = await row.fetchone()
            return result

    async def fetch_all(
        self,
        query: str,
        params: Mapping[str, Any] | None = None,
    ) -> Iterable[Mapping[str, Any]]:
        async with self.__pool.connection() as conn:
            cursor = await conn.execute(query, params)
            return await cursor.fetchall()

    async def close(self) -> None:
        """
        Close the connection pool.
        Must be called only on application shutdown.
        """
        await self.__pool.close()

    @property
    def pool(self) -> AsyncConnectionPool:
        """
        Exposes the underlying pool for advanced use cases.
        """
        return self.__pool

    def __repr__(self) -> str:
        return "AdapterPostgres(psycopg3)"
