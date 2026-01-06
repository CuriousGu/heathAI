from abc import ABC, abstractmethod
from langchain_core.messages import AIMessage
from langchain_core.runnables.config import RunnableConfig
from langchain_core.language_models.base import LanguageModelInput
from typing import Any


class LLMInterface(ABC):
    """
    Contract that any Large Language Model must implement
    in order to be used by the domain and application layers.
    """
    @abstractmethod
    def __init__(self, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def invoke(
        input: LanguageModelInput,
        config: RunnableConfig | None = None,
        *,
        stop: list[str] | None = None,
        **kwargs: Any,
    ) -> AIMessage:
        pass

    @abstractmethod
    async def ainvoke(
        input: LanguageModelInput,
        config: RunnableConfig | None = None,
        *,
        stop: list[str] | None = None,
        **kwargs: Any,
    ) -> AIMessage:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
