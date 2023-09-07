import asyncio

from pymongo import UpdateOne
from structlog import get_logger

from pokemon.apps.pokemon_api.repository import pokemon_repository
from pokemon.core.mongodb import get_database

logger = get_logger(__name__)


async def prefill_database_with_pokemons():
    await logger.ainfo("Start prefilling pokemon database")
    poke_tasks = [
        asyncio.create_task(pokemon_repository.get_pokemon_info(idx))
        for idx in range(1, 151)
    ]
    pokemons = await asyncio.gather(*poke_tasks)
    updations = [
        UpdateOne({"name": poke.get("name")}, {"$set": poke}, upsert=True)
        for poke in pokemons
    ]

    db = await get_database()
    collection = db["pokemons"]
    await collection.bulk_write(updations)
    await logger.ainfo("Successfull prefilling pokemon database")
