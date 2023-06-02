from aioredis import from_url

from app.api.config.base import REDIS_URL
from app.api.redis.services import RedisService


async def init_redis_pool():
    redis = await from_url(
        REDIS_URL,
        encoding="utf-8",
        decode_responses=True,
    )
    RedisCache.init(RedisService(redis))


class RedisCache:
    """
        RedisCache
    """
    _core = None
    _prefix = None
    _expire = None
    _init = False

    @classmethod
    def init(
        cls,
        core,
        prefix: str = "",
        expire: int = None,
    ):
        if cls._init:
            return
        cls._init = True
        cls._core = core
        cls._prefix = prefix
        cls._expire = expire

    @classmethod
    def core(cls):
        return cls._core
