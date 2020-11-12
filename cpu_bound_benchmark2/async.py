import asyncio
import time

import aiohttp


def is_prime(number):
    for i in range(number - 1, 1, -1):
        if number % i == 0:
            return True
    print(f'{number} is not prime')
    return False


async def hello():
    is_prime(16769023)

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[session.get('https://google.com') for _ in range(10)]
        )
        print([(await r.text())[:20] for r in results])

    is_prime(16769023)


async def main():
    start = time.time()
    tasks = [hello() for _ in range(5)]
    await asyncio.gather(*tasks)
    print(time.time() - start)


if __name__ == '__main__':
    asyncio.run(main())
