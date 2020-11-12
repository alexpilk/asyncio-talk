import asyncio
import time


class SyncCat:
    def __init__(self, name):
        self.name = name

    async def exist(self):
        self._eat()
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self._have_free_time)

    def _eat(self):
        print(f'{self.name} eating')

    # ouch
    def _have_free_time(self):
        print(f'{self.name} got some free time')
        self._sleep()

    def _sleep(self):
        print(f'{self.name} sleeping')
        time.sleep(2)
        print(f'{self.name} woke up')


async def main():
    cats = [SyncCat(_) for _ in range(5)]
    await asyncio.gather(*(cat.exist() for cat in cats))


asyncio.run(main())
