import asyncio
import time


def is_prime(number):
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            return True
    return False


async def hello():
    await asyncio.sleep(1)
    is_prime(16769023)


async def main():
    tasks = [hello() for _ in range(5)]
    start = time.time()
    await asyncio.gather(*tasks)
    print(time.time() - start)


asyncio.run(main())
