import os
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    server_host: str = os.getenv("SERVER_HOST")
    server_port: int = os.getenv("SERVER_PORT")
    database_url: str = os.getenv("DATABASE_URL")


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)