import asyncio
import time


def sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        yield


def hello():
    print('Hello')
    yield from sleep(1)
    print('Goodbye')


async def main():
    await asyncio.gather(hello(), hello())


asyncio.run(main())
