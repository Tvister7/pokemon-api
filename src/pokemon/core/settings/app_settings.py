from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    host: str = Field("0.0.0.0")
    port: int = Field(9000)
    environment: str = Field("dev")

    pokemon_url: str = Field("https://pokeapi.co/")

    model_config = SettingsConfigDict(
        env_prefix="app_", env_file=".env", env_file_encoding="utf-8"
    )


app_settings = AppSettings()  # type: ignore
