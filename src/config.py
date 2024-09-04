from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    MODE: str = 'DEV'

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str


load_dotenv(find_dotenv('.env'))
settings = Settings()
