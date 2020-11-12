
def even_numbers_until(start, limit):
    for number in range(start, limit):
        if number % 2 == 0:
            yield number


generator = even_numbers_until(0, 10)
another_generator = even_numbers_until(100, 110)


def gather(generators):
    while True:
        if not generators:
            break
        for i, g in enumerate(generators):
            try:
                print(next(g))
            except StopIteration:
                del generators[i]


gather([generator, another_generator])
