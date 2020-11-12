import asyncio
import time


async def hello():
    print('Hello')
    time.sleep(1)
    print('Goodbye')


async def main():
    await asyncio.gather(hello(), hello())


asyncio.run(main())
