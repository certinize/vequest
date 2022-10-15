import fastapi

from app import db, settings


def create_db_client(app: fastapi.FastAPI) -> None:
    assert settings.app_settings.database_url is not None
    app.state.db = db.Database(settings.app_settings.database_url)


def create_start_app_handler(app: fastapi.FastAPI):
    def start_app() -> None:
        create_db_client(app)

    return start_app
