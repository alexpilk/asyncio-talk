
def even_numbers_until(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number


for even_number in even_numbers_until(99999999):
    print(even_number)
