import time


def hello():
    print('Hello')
    start_time = time.time()
    while time.time() - start_time < 1:
        yield
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
