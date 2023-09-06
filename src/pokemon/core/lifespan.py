from contextlib import asynccontextmanager

from fastapi import FastAPI

from pokemon.apps.pokemon_api.commands import prefill_database_with_pokemons
from pokemon.core.mongodb import close_mongo_connection, connect_to_mongo
from pokemon.core.signals import bind_signals


@asynccontextmanager
async def lifespan(app: FastAPI):
    await bind_signals()
    await connect_to_mongo()
    await prefill_database_with_pokemons()
    yield
    await close_mongo_connection()
