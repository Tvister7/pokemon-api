from fastapi import FastAPI

from pokemon.core.routers import init_routers
from pokemon.core.lifespan import lifespan


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    init_routers(app)
    return app
