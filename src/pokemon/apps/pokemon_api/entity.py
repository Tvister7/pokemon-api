from typing import Any

from pydantic import BaseModel


class FormEntity(BaseModel):
    name: str
    url: str


class AbilityModel(BaseModel):
    name: str
    url: str


class AbilityEntity(BaseModel):
    ability: AbilityModel
    is_hidden: bool
    slot: int


class IndexVersion(BaseModel):
    name: str
    url: str


class IndexEntity(BaseModel):
    game_index: int
    version: IndexVersion


class StatEntity(BaseModel):
    name: str
    url: str


class StatModel(BaseModel):
    base_stat: int
    effort: int
    stat: StatEntity


class TypeEntity(BaseModel):
    name: str
    url: str


class TypeModel(BaseModel):
    slot: int
    type: TypeEntity


class PokemonClientEntity(BaseModel):
    abilities: list[AbilityEntity]
    base_experience: int
    forms: list[FormEntity]
    game_indices: list[IndexEntity]
    height: int
    held_items: list
    id: int
    is_default: bool
    location_area_encounters: str
    moves: list
    name: str
    order: int
    past_types: list
    sprites: dict[str, Any]
    stats: list[StatModel]
    types: list[TypeModel]
