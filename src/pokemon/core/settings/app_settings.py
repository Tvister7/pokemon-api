from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 9000

    model_config = SettingsConfigDict(
        env_prefix="app_", env_file=".env", env_file_encoding="utf-8"
    )


app_settings = AppSettings()  # type: ignore
