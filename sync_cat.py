import time
import asyncio


class SyncCat:

    def exist(self):
        self._eat()
        self._have_free_time()

    def _eat(self):
        print('eating')

    def _have_free_time(self):
        print('got some free time')
        self._sleep()

    def _sleep(self):
        print('sleeping')
        time.sleep(2)
        print('woke up')


class AsyncCat(SyncCat):

    async def exist(self):
        self._eat()
        await self._have_free_time()

    async def _have_free_time(self):
        print('got some free time')
        await self._sleep()

    async def _sleep(self):
        print('sleeping')
        await asyncio.sleep(1)
        print('woke up')


cats = [AsyncCat() for _ in range(5)]


async def main(cats):
    await asyncio.gather(*[cat.exist() for cat in cats])


asyncio.run(main(cats))
