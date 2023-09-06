from sys import exit

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from structlog import getLogger

from pokemon.core.settings.mongo_settings import mongo_settings

logger = getLogger(__name__)


class DataBase:
    client: AsyncIOMotorClient = None  # type: ignore
    db: AsyncIOMotorDatabase = None  # type: ignore


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.db  # type: ignore


async def get_client() -> AsyncIOMotorClient:
    return db.client  # type: ignore


async def connect_to_mongo():
    await logger.adebug("initializing mongo connection")
    try:
        db.client = AsyncIOMotorClient(mongo_settings.url.unicode_string())
        db.db = db.client[mongo_settings.database]
    except Exception as exc:  # pylint: disable=broad-except
        await logger.aerror("Failed connect to mongo", exc=str(exc))
        exit(1)
    await logger.adebug("successfully initialized mongo connection")


async def close_mongo_connection():
    await logger.adebug("closing mongo connection")
    db.client.close()
