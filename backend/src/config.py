import os
from pydantic_settings import BaseSettings


basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    basedir: str = basedir
    app_name: str = 'Brain Panic'
    session_ttl: int = 24  # session time to live in hours
    secret_key: str
    database_uri: str


settings = Settings()
