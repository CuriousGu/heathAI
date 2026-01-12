from typing import Optional
import logging

from app.interfaces.sql import DatabaseInterface
from app.infra.adapter.sql.postgres import AdapterPostgres
from app.settings.config import settings


_db_instance: Optional[DatabaseInterface] = None
logger = logging.getLogger(__name__)


def get_sql() -> DatabaseInterface:
    global _db_instance

    if _db_instance is not None:
        return _db_instance

    if settings.DATABASE_PROVIDER == "postgres":
        _db_instance = AdapterPostgres()
    else:
        raise ValueError("Invalid database provider")

    logger.info(f"Using database: {_db_instance!r}")
    return _db_instance
