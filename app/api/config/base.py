from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret


API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "0.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)
PROJECT_NAME: str = config("PROJECT_NAME", default="SC Worker Server")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

# Redis
REDIS_URL = config("REDIS_URL")

# DB values
# POSTGRES_USER: str = config("POSTGRES_USER")
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
# POSTGRES_SERVER: str = config("POSTGRES_SERVER", default="localhost")
# POSTGRES_PORT: str = config("POSTGRES_PORT", default=5432)
# POSTGRES_DB: str = config("POSTGRES_DB", default="flash")
# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

