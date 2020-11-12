import asyncio
import aiohttp
import time


async def hello():
    async with aiohttp.ClientSession() as session:
        await session.get('https://google.com')


async def main():
    tasks = [hello() for _ in range(200)]
    start = time.time()
    await asyncio.gather(*tasks)
    print(time.time() - start)


asyncio.run(main())
