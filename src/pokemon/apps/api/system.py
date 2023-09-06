from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from structlog import get_logger

from pokemon.core.mongodb import get_client

logger = get_logger(__name__)

router = APIRouter()


@router.get("/liveness/", name="liveness", summary="Статус веб-приложения")
async def liveness():
    return PlainTextResponse("OK")


@router.get("/readiness/", name="liveness", summary="Статус базы данных")
async def readiness():
    try:
        client = await get_client()
        await client.admin.command("ping")
        return PlainTextResponse("OK")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal error")


@router.get("/exception/", name="exception", summary="Провера ошибки")
async def exception():
    11 / 0  # noqa


@router.get(
    "/structlog_exception/", name="exception", summary="Провера пойманной ошибки"
)
async def structlog_exception():
    try:
        11 / 0  # noqa
    except Exception:
        await logger.aexception("Structlog exception")
    return PlainTextResponse("error", status_code=500)
