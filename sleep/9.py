import time


def sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        yield


def hello():
    print('Hello')
    yield from sleep(1)
    print('Goodbye')


def gather(generators):
    while True:
        if not generators:
            break
        for i, g in enumerate(generators):
            try:
                next(g)
            except StopIteration:
                del generators[i]


gather([hello(), hello()])
