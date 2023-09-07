from fastapi import FastAPI

from pokemon.core.lifespan import lifespan
from pokemon.core.routers import init_routers


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    init_routers(app)
    return app
