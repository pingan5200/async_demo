import time
import threading
import logging
import random
import sys
from threading import Thread

# https://docs.python.org/3/c-api/init.html#thread-state-and-the-global-interpreter-lock
# https://www.dabeaz.com/python/GIL.pdf

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s: %(message)s',
)

def countdown(n):
    while n > 0:
        # print(f'{threading.current_thread().name}-倒数开始：', n)
        logging.debug(f'倒数开始：{n}')
        n -= 1
        time.sleep(1)


# threading.current_thread().name
def worker():
    print(threading.current_thread().name, '开始')
    time.sleep(0.5)
    print(threading.current_thread().name, '结束')


class MyThread(Thread):
    def __init__(self, name, count):
        Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        try:
            lock.acquire()
            logging.debug('lock...')
            countdown(self.count)
        finally:
            lock.release()
            logging.debug('open again')


# lock = threading.Lock()
lock = threading.RLock()  # re...Factory function that returns a new reentrant lock
TOTAL = 0


def add_plus_8():
    global TOTAL
    with lock:
        TOTAL += 8


def add_plus():
    global TOTAL
    # lock.acquire()
    with lock:
        logging.debug(f'before add: {TOTAL}')
        wait = random.randint(1, 3)
        time.sleep(wait)
        print(f'执行了{wait}s之后...')
        TOTAL += 1
        logging.debug(f'after add: {TOTAL}')

        add_plus_8()
    # lock.release()


def main():
    # Thread(target=worker, name='de8ug-thread').start()
    thread_list = []
    logging.debug('start...')
    for i in range(int(sys.argv[1])):
        # t = Thread(target=countdown, args=(3, ))
        # t = MyThread(f'thread-{i+1}', 3)
        t = Thread(target=add_plus)
        t.start()
        thread_list.append(t)
        # t.join()  # Wait until the thread terminates.
    
    for i in thread_list:
        i.join()

    logging.debug('end.')

    
if __name__ == '__main__':
    main()