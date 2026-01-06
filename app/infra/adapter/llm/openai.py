from app.interfaces.llm.interface import LLMInterface
from app.interfaces.llm.models import LLMResponse
from app.settings.config import settings

from langchain_openai import ChatOpenAI


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
            openai_api_key=settings.OPENAI_API_KEY,
            model_kwargs={
                "validate_openai_api_key": True
            }
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

    @property
    def model(self) -> ChatOpenAI:
        """Returns the underlying ChatOpenAI model instance."""
        return self.__client

    def __repr__(self) -> str:
        return f"AdapterOpenAI(model={self.__client.model_name})"
