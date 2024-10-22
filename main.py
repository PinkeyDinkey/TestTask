"""Модуль запуска сервиса"""

from os import system

from uvicorn import run

from service import create_app
from settings import settings

app = create_app()

if __name__ == "__main__":
    if settings.s_env == "DEV":
        run(app, host=settings.s_host, port=settings.s_port, workers=1)
    else:
        system(
            f"uvicorn main:app "
            f"--host {settings.s_host} "
            f"--port {settings.s_port} "
            f"--workers {settings.max_workers_count}"
        )
