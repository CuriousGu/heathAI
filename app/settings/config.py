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

    # Database (variables usadas no adapter)
    PSQL_USERNAME_MEMORY: str
    PSQL_PASSWORD_MEMORY: str
    PSQL_HOST_MEMORY: str
    PSQL_PORT_MEMORY: int
    PSQL_DATABASE_MEMORY: str
    PSQL_SSLMODE_MEMORY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
