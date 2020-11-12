
def even_numbers_until(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number


generator = even_numbers_until(10)

while True:
    try:
        print(next(generator))
    except StopIteration:
        break
