import multiprocessing
import time


def is_prime(number):
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            return True
    return False


def hello():
    time.sleep(1)
    is_prime(16769023)


def smap(f):
    return f()


def main():
    start = time.time()
    with multiprocessing.Pool(5) as pool:
        pool.map(smap, [hello for _ in range(5)])
    print(time.time() - start)


if __name__ == '__main__':
    main()
