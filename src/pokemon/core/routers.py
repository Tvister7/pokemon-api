from fastapi import APIRouter, FastAPI

from pokemon.apps.api.system import router as system_router
from pokemon.apps.api.v1.views import router as pokemon_router


def init_routers(app: FastAPI) -> FastAPI:
    app.include_router(
        system_router,
        prefix="/system",
        tags=["system"],
    )
    app.include_router(get_v1_router())

    return app


def get_v1_router() -> APIRouter:
    v1_router = APIRouter(prefix="/v1")
    v1_router.include_router(
        pokemon_router,
        prefix="/pokemon",
        tags=["pokemon"],
    )

    return v1_router
