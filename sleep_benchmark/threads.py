import threading
import time


def hello():
    time.sleep(3)


def main():
    threads = [threading.Thread(target=hello) for _ in range(4000)]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(time.time() - start)


main()
