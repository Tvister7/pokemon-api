from httpx import AsyncClient
from structlog import get_logger

from pokemon.apps.pokemon_api.entity import PokemonClientEntity
from pokemon.core.settings.app_settings import app_settings


class PokemonRepository:
    def __init__(self):
        self.client = AsyncClient(
            base_url=app_settings.pokemon_url,
        )
        self.logger = get_logger(__name__, service="pokemon_api")

    async def get_pokemon_info(self, pokemon_number: int) -> PokemonClientEntity:
        response = await self.client.get(f"/api/v2/pokemon/{pokemon_number}")
        return response.json()
        # return PokemonClientEntity(**(response.json()))

    async def get_client(self):
        async with self.client as client:
            yield client


pokemon_repository = PokemonRepository()
