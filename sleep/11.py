import asyncio
import time


async def sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        await asyncio.sleep(0)


async def hello():
    print('Hello')
    await sleep(1)
    print('Goodbye')


async def main():
    await asyncio.gather(hello(), hello())


asyncio.run(main())
