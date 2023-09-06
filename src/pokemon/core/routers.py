from fastapi import FastAPI

from pokemon.apps.api.system import router as system_router


def init_routers(app: FastAPI) -> FastAPI:
    app.include_router(
        system_router,
        prefix="/system",
        tags=["system"],
    )
    return app
