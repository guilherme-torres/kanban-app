import os
from pydantic_settings import BaseSettings, SettingsConfigDict


basedir = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(basedir, '.env')

class JWTConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_path)

    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRES_SECONDS: int
