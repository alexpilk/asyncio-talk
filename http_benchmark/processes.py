import multiprocessing
import time
import requests


def hello():
    with requests.Session() as session:
        session.get('https://google.com')


def smap(f):
    return f()


def main():
    with multiprocessing.Pool(200) as pool:
        start = time.time()
        pool.map(smap, [hello for _ in range(200)])
    print(time.time() - start)


if __name__ == '__main__':
    main()
