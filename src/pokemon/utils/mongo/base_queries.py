from typing import Any

from structlog import get_logger

from pokemon.apps.pokemon_api.entity import PokemonClientEntity
from pokemon.core.mongodb import get_database
from pokemon.utils.mongo.exceptions import MongoNotFoundException

logger = get_logger(__name__)


async def get_single_pokemon_from_mongo(query: dict[str, Any]) -> PokemonClientEntity:
    db = await get_database()
    collection = db["pokemons"]
    result = await collection.find_one(query)

    if not result:
        msg = f"Could not find pokemon with {query}"
        logger.warning("Mongo find error", msg=msg)
        raise MongoNotFoundException(msg)

    return PokemonClientEntity(**result)


async def get_multiple_pokemons_from_mongo(
    query: dict[str, Any]
) -> list[PokemonClientEntity]:
    db = await get_database()
    collection = db["pokemons"]
    results = collection.find(query)

    result_list = []

    async for result in results:
        result_list.append(PokemonClientEntity(**result))

    if not result_list:
        msg = f"Could not find pokemon with {query}"
        logger.warning("Mongo find error", msg=msg)
        raise MongoNotFoundException(msg)

    return result_list
