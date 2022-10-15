# using pydantic load .env file
import pydantic


class Settings(pydantic.BaseSettings):
    database_url: pydantic.PostgresDsn | None = None

    class Config(pydantic.BaseSettings.Config):
        env_file = ".env"


app_settings = Settings()
