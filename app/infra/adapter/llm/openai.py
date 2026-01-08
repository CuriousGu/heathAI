from app.interfaces.llm.interface import LLMInterface
from app.interfaces.llm.models import LLMResponse
from app.settings.config import settings

from langchain_core.runnables.base import Runnable
from langchain_core.language_models import LanguageModelInput
from langchain_core.tools import BaseTool
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI
from langchain_openai.chat_models.base import (
    _DictOrPydantic,
    _DictOrPydanticClass
)
from typing import Any, Literal
from collections.abc import Callable, Sequence


class AdapterOpenAI(LLMInterface):
    """
    OpenAI implementation of the LLMInterface.
    This class is part of the infrastructure layer and
    contains all provider-specific logic.
    """
    def __init__(self) -> None:
        self.__client = ChatOpenAI(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            openai_api_key=settings.OPENAI_API_KEY
        )

    async def ainvoke(self, input, config=None, *, stop=None, **kwargs):
        return await self.__client.ainvoke(
            input,
            config=config,
            stop=stop,
            **kwargs,
        )

    def invoke(self, input, config=None, *, stop=None, **kwargs):
        return self.__client.invoke(
            input,
            config=config,
            stop=stop,
            **kwargs,
        )

    def bind_tools(
        self,
        tools: Sequence[dict[str, Any] | type | Callable | BaseTool],
        *,
        tool_choice: dict | str | bool | None = None,
        strict: bool | None = None,
        parallel_tool_calls: bool | None = None,
        response_format: _DictOrPydanticClass | None = None,
        **kwargs: Any,
    ) -> Runnable[LanguageModelInput, AIMessage]:
        return self.__client.bind_tools(
            tools,
            tool_choice=tool_choice,
            strict=strict,
            parallel_tool_calls=parallel_tool_calls,
            response_format=response_format,
            **kwargs,
        )

    def with_structured_output(
        self,
        schema: _DictOrPydanticClass | None = None,
        *,
        method: Literal["function_calling", "json_mode", "json_schema"] = "json_schema",
        include_raw: bool = False,
        strict: bool | None = None,
        tools: list | None = None,
        **kwargs: Any,
    ) -> Runnable[LanguageModelInput, _DictOrPydantic]:
        return self.__client.with_structured_output(
            schema,
            method=method,
            include_raw=include_raw,
            strict=strict,
            tools=tools,
            **kwargs,
        )

    @property
    def model(self) -> ChatOpenAI:
        """Returns the underlying ChatOpenAI model instance."""
        return self.__client

    def __repr__(self) -> str:
        return f"AdapterOpenAI(model={self.__client.model_name})"
