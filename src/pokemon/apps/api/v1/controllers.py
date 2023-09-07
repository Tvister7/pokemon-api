from fastapi import HTTPException
from structlog import get_logger

from pokemon.apps.api.v1.models import (
    OutputPokemonAbilityModel,
    OutputPokemonModel,
    OutputPokemonStatModel,
)
from pokemon.apps.pokemon_api.entity import PokemonClientEntity
from pokemon.utils.mongo.exceptions import MongoNotFoundException
from pokemon.utils.mongo.queries import (
    filter_pokemon_names_from_mongo_by_hp,
    get_pokemon_from_mongo_by_name,
)

logger = get_logger(__name__)


async def get_pokemon_by_name_controller(name: str) -> OutputPokemonModel:
    try:
        db_result: PokemonClientEntity = await get_pokemon_from_mongo_by_name(name)
    except MongoNotFoundException:
        raise HTTPException(status_code=404, detail=f"Couldn't find Pokemon {name}")

    abilities = [
        OutputPokemonAbilityModel(
            ability_name=db_ability.ability.name, ability_url=db_ability.ability.url
        )
        for db_ability in db_result.abilities
    ]

    stat_dict = {
        db_stat.stat.name: db_stat.base_stat + db_stat.effort
        for db_stat in db_result.stats
    }

    return OutputPokemonModel(
        name=db_result.name,
        abilities=abilities,
        stats=OutputPokemonStatModel(**stat_dict),
    )


async def filter_pokemons_by_max_hp_controller(hp) -> list[str]:
    try:
        db_result: list[str] = await filter_pokemon_names_from_mongo_by_hp(hp)
    except MongoNotFoundException:
        raise HTTPException(
            status_code=404, detail=f"Couldn't find Pokemons with {hp=} or more"
        )

    return db_result
