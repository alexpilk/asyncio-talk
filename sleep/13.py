import time
import threading


def hello():
    print('Hello')
    time.sleep(1)
    print('Goodbye')


def main():
    hello_1 = threading.Thread(target=hello)
    hello_2 = threading.Thread(target=hello)
    hello_1.start()
    hello_2.start()


main()
