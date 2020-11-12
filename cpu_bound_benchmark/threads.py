import threading
import time


def is_prime(number):
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            return True
    return False


def hello():
    time.sleep(1)
    is_prime(16769023)


def main():
    threads = [threading.Thread(target=hello) for _ in range(5)]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(time.time() - start)


main()
