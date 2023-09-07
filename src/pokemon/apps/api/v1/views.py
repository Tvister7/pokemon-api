from fastapi import APIRouter

from pokemon.apps.api.v1.controllers import (
    filter_pokemons_by_max_hp_controller,
    get_pokemon_by_name_controller,
)
from pokemon.apps.api.v1.models import OutputPokemonModel

router = APIRouter()


@router.get("/{name}")
async def get_pokemon_by_name(name: str) -> OutputPokemonModel:
    return await get_pokemon_by_name_controller(name)


@router.get("/hp-filter/{hp}")
async def filter_pokemons_by_max_hp(hp: int) -> list[str]:
    return await filter_pokemons_by_max_hp_controller(hp)
