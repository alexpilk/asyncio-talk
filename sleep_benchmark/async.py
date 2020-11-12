import asyncio
import time


async def hello():
    await asyncio.sleep(3)


async def main():
    tasks = [hello() for _ in range(4000)]
    start = time.time()
    await asyncio.gather(*tasks)
    print(time.time() - start)


asyncio.run(main())
