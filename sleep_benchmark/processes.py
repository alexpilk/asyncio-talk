import multiprocessing
import time


def hello():
    time.sleep(3)


def smap(f):
    return f()


def main():
    with multiprocessing.Pool() as pool:
        start = time.time()
        pool.map(smap, [hello for _ in range(4000)])
    print(time.time() - start)


if __name__ == '__main__':
    main()
