from langchain_ollama import ChatOllama

from app.interfaces.llm.interface import LLMInterface
from app.settings.config import settings


class AdapterOllama(LLMInterface):
    """
    Ollama implementation of the LLMInterface.
    This class is part of the infrastructure layer and
    contains all provider-specific logic.
    """

    def __init__(self):
        self.client = ChatOllama(
            model=settings.LLM_MODEL,
            base_url=settings.OLLAMA_BASE_URL
        )
        self.model = settings.LLM_MODEL

    def generate(
        self,
        prompt: str,
        *,
        temperature: float = 0.0,
        max_tokens: int = 512,
        metadata: dict | None = None
    ) -> LLMResponse:
        """
        Calls the Ollama Chat Completions API and adapts
        the response to the interfaces LLMResponse format.
        """
        return "oi"
