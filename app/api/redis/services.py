class RedisService:
    """
        Redis cache global service events. All the redis cache events are mentioned here

        Events mentioned in this method:
        Methods:
            set -> set the key value pair in redis.
            get -> get the key value from redis.
            delete -> delete the key from redis.
    """

    def __init__(self, redis) -> None:
        self._redis = redis

    async def set(self, key, value):
        await self._redis.set(key, value)
        return await self._redis.get(key)

    async def get(self, key):
        return await self._redis.get(key)

    async def delete(self, key):
        return await self._redis.delete(key)
