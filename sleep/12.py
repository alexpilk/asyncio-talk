import asyncio


async def hello():
    print('Hello')
    await asyncio.sleep(1)
    print('Goodbye')


async def main():
    await asyncio.gather(hello(), hello())


asyncio.run(main())
