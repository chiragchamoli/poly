from typing import Callable

from fastapi import FastAPI
from app.api.redis.connection import init_redis_pool


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await init_redis_pool()
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await app.state.redis.close()
    return stop_app
