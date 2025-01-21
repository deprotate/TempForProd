from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_addres: str= "0.0.0.0:8080"
    db_url: str = "postgresql+asyncpg://postgres:admin@localhost:5432/tink"
    echo: bool = True



settings = Settings()