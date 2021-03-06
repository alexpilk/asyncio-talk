import threading
import time

import requests


def is_prime(number):
    for i in range(number - 1, 1, -1):
        if number % i == 0:
            return True
    print(f'{number} is not prime')
    return False


def hello():
    is_prime(16769023)

    with requests.Session() as session:
        results = [
            session.get('https://google.com') for _ in range(10)
        ]
        print([r.text[:20] for r in results])

    is_prime(16769023)


def main():
    threads = [threading.Thread(target=hello) for _ in range(5)]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(time.time() - start)


if __name__ == '__main__':
    main()
