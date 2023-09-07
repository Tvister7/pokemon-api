from structlog import get_logger

from pokemon.apps.pokemon_api.entity import PokemonClientEntity
from pokemon.core.mongodb import get_database
from pokemon.utils.mongo.base_queries import get_single_pokemon_from_mongo
from pokemon.utils.mongo.exceptions import MongoNotFoundException

logger = get_logger(__name__)


async def get_pokemon_from_mongo_by_name(name: str) -> PokemonClientEntity:
    query = {"name": name}
    return await get_single_pokemon_from_mongo(query)


async def filter_pokemon_names_from_mongo_by_hp(hp: int) -> list[str]:
    pipeline = [
        {"$unwind": "$stats"},
        {"$match": {"stats.stat.name": "hp"}},
        {"$addFields": {"full_hp": {"$sum": ["$stats.base_stat", "$stats.effort"]}}},
        {"$match": {"full_hp": {"$gt": hp}}},
        {"$project": {"name": 1, "_id": 0}},
    ]

    db = await get_database()
    collection = db["pokemons"]
    results = collection.aggregate(pipeline)

    result_list = []

    async for result in results:
        result_list.append(result.get("name"))

    if not result_list:
        msg = f"Could not find pokemon with {hp=} or more"
        logger.warning("Mongo find error", msg=msg)
        raise MongoNotFoundException(msg)

    return result_list
