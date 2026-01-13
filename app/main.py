from app.api.routes import test_router, messages_router
from app.settings.config import settings

from app.settings.logging import setup_logging
from app.infra.factory.llm import get_llm
from app.infra.factory.sql import get_sql
from app.services.agents.graph import Graph

from fastapi import FastAPI


setup_logging(settings.LOG_LEVEL)

_ = get_sql()  # Pre-initialize SQL database at startup
_ = get_llm()  # Pre-initialize LLM at startup
_ = Graph()  # Pre-initialize Agent Graph at startup


def create_api():
    app = FastAPI(title="HeathAI", version="0.1")

    app.include_router(test_router)
    app.include_router(messages_router)

    return app


app = create_api()
