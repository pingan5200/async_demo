import time
import threading
from threading import Thread


def countdown(n, number):
    while n > 0:
        print(f'第{number}个线程，倒数开始：', threading.current_thread().name, n)
        n -= 1
        time.sleep(1)


# threading.current_thread().name
def worker():
    print(threading.current_thread().name, '开始')
    time.sleep(0.5)
    print(threading.current_thread().name, '结束')


def main():
    Thread(target=worker, name='de8ug-thread').start()
    for i in range(3):
        t = Thread(target=countdown, args=(5, i+1))
        t.start()

    
if __name__ == '__main__':
    main()