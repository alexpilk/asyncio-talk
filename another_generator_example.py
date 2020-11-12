import time


def sleep(seconds):
    start = time.time()
    while time.time() - start < seconds:
        yield


def count_to_ten():
    print(1)
    yield from sleep(1)
    print(2)
    yield from sleep(1)
    print(3)
    yield from sleep(1)
    print(4)
    yield from sleep(1)
    print(5)


def loop(tasks):
    while True:
        for task in tasks:
            next(task)


loop([count_to_ten(), count_to_ten()])

