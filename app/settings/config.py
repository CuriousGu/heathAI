from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # GenAI
    LLM_PROVIDER: str
    LLM_MODEL: str
    LLM_URL: str | None = None
    LLM_TEMPERATURE: float = 0.1

    OPENAI_API_KEY: str

    # Logs
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
