"""Application module."""

from fastapi import FastAPI

from containers import Container
from endpoints import router


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container
    app.include_router(router)
    return app

app = create_app()