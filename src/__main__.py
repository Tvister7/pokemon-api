from uvicorn import run

from pokemon.asgi import app
from pokemon.core.settings.app_settings import app_settings

if __name__ == "__main__":
    run(app, host=app_settings.host, port=app_settings.port)
