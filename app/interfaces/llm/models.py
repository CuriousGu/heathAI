from dataclasses import dataclass, field
from typing import Mapping, Any, Optional


@dataclass(frozen=True)
class LLMResponse:
    content: str
    raw: Optional[Mapping[str, Any]] = field(default=None, repr=False)
