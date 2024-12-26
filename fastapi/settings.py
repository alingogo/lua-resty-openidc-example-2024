from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PLATFORM: str

settings = Settings()