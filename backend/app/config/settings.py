import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


settings = Settings(
    database_url=os.getenv("DATABASE_URL", ""),
    secret_key=os.getenv("SECRET_KEY", ""),
    algorithm=os.getenv("ALGORITHM", "HS256"),
    access_token_expire_minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")),
)
