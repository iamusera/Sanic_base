import os
import asyncio
import asyncio_redis


class RedisSession:
    """
    建立redis连接池
    """
    _pool = None

    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host=str(os.getenv('REDIS_ENDPOINT', "localhost")), port=int(os.getenv('REDIS_PORT', 6379)),
                poolsize=int(os.getenv('REDIS_POOLSIZE', 10)),
                password=os.getenv('REDIS_PASSWORD', ''),
                db=os.getenv('REDIS_DB', 2)
            )

        return self._pool


redis_session = RedisSession()
redis_pool = redis_session.get_redis_pool


if __name__ == '__main__':

    async def do_set():
        redis_connection = await redis_pool()
        # await redis_connection.set('name', 'name1')
        res = await redis_connection.get('52066a88-ceed-4f18-923f-9917f867c5ec')
        print("get name: {0}".format(res))
        return res
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_set())
