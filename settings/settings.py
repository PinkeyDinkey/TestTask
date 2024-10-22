"""Построение объекта конфигурации сервиса из файла конфигурации"""

from os import environ
from pathlib import Path
from typing import List, Literal
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Класс объекта конфигурации сервиса из файла конфигурации"""

    # Service config
    s_host: str = "localhost"
    s_port: int = 1234
    s_origins: List[str] = ["*"]
    max_workers_count: int = 4
    s_env: Literal["DEV", "PRODUCTION"] = "PRODUCTION"
    s_log_level: Literal["CRITICAL", "FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG", "NOTSET"] = (
        "DEBUG"
    )

    # Data base config
    db_host: str = "0.0.0.0"
    db_port: int = 5432
    db_username: str = "postgres"
    db_password: str = "password"
    db_name: str = "db_name"


    def __init__(self):
        # Настройка сервиса
        self.s_host = environ.get("SERVICE_HOST", self.s_host)
        self.s_port = int(environ.get("SERVICE_PORT", self.s_port))
        self.s_origins = environ.get("SERVICE_ORIGINS", self.s_origins)
        self.max_workers_count = environ.get("SERVICE_MAX_WORKERS_COUNT", self.max_workers_count)
        self.s_env = environ.get("SERVICE_ENV", self.s_env)
        self.s_log_level = environ.get("SERVICE_LOG_LEVEL", self.s_log_level)

        # Настройка подключения к бд
        self.db_host = environ.get("DB_HOST", self.db_host)
        self.db_port = int(environ.get("DB_PORT", self.db_port))
        self.db_username = environ.get("DB_USERNAME", self.db_username)
        self.db_password = environ.get("DB_PASSWORD", self.db_password)
        self.db_name = environ.get("DB_NAME", self.db_name)



settings = Settings()
