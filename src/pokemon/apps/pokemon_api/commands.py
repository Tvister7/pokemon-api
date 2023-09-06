import asyncio

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
    db = await get_database()
    collection = db["pokemons"]
    await collection.insert_many(pokemons)
    await logger.ainfo("Successfull prefilling pokemon database")
