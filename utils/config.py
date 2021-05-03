from pydantic import BaseSettings


class Settings(BaseSettings):
    message: str
    jwt_secret: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
