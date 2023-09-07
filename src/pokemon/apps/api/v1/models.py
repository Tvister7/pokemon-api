from pydantic import BaseModel, ConfigDict


class OutputPokemonAbilityModel(BaseModel):
    ability_name: str
    ability_url: str


class OutputPokemonStatModel(BaseModel):
    hp: int
    attack: int
    defense: int
    speed: int

    model_config = ConfigDict(extra="allow")


class OutputPokemonModel(BaseModel):
    name: str
    abilities: list[OutputPokemonAbilityModel]
    stats: OutputPokemonStatModel
