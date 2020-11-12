import threading
import time

import requests


def hello():
    with requests.Session() as session:
        session.get('https://google.com')


def main():
    threads = [threading.Thread(target=hello) for _ in range(200)]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(time.time() - start)


main()
