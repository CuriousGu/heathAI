from typing import Optional

from app.interfaces.llm.interface import LLMInterface
from app.infra.adapter.llm import AdapterOpenAI, AdapterOllama
from app.settings.config import settings

_llm_instance: Optional[LLMInterface] = None


def get_llm() -> LLMInterface:
    global _llm_instance

    if _llm_instance is not None:
        return _llm_instance

    if settings.LLM_PROVIDER == "openai":
        _llm_instance = AdapterOpenAI()
    elif settings.LLM_PROVIDER == "ollama":
        _llm_instance = AdapterOllama()
    else:
        raise ValueError("Invalid LLM provider")

    return _llm_instance
