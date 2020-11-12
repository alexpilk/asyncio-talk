import time


def hello():
    print('Hello')
    yield
    time.sleep(1)
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
