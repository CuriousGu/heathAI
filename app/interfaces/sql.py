from abc import ABC, abstractmethod
from typing import Any, Iterable, Mapping


class DatabaseInterface(ABC):
    """
    Contract that any relational database adapter must implement
    in order to be used by the domain and application layers.
    """

    @abstractmethod
    def __init__(self, **kwargs: Any) -> None:
        pass

    @abstractmethod
    async def execute(
        self,
        query: str,
        *args: Any,
    ) -> None:
        """
        Execute a statement that does not return rows.
        """
        pass

    @abstractmethod
    async def fetch_one(
        self,
        query: str,
        *args: Any,
    ) -> Mapping[str, Any] | None:
        """
        Execute a query and return a single row.
        """
        pass

    @abstractmethod
    async def fetch_all(
        self,
        query: str,
        *args: Any,
    ) -> Iterable[Mapping[str, Any]]:
        """
        Execute a query and return multiple rows.
        """
        pass

    @abstractmethod
    async def transaction(self):
        """
        Return an async transaction context manager.
        """
        pass

    @abstractmethod
    async def close(self) -> None:
        """
        Close all connections or pools.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
