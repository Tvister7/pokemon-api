from pydantic import Field, MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoSettings(BaseSettings):
    url: MongoDsn = Field("mongodb://root:example@mongo:27017/")
    database: str = "pokemon"

    model_config = SettingsConfigDict(
        env_prefix="mongo_", env_file=".env", env_file_encoding="utf-8"
    )


mongo_settings = MongoSettings()  # type: ignore
