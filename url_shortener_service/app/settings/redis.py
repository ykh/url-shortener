import os

from redis import asyncio as aioredis


class Redis:
    @staticmethod
    async def get_redis():
        redis_client = await aioredis.from_url(os.getenv("REDIS_URL"))

        try:
            yield redis_client
        finally:
            await redis_client.close()
