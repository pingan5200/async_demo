import time
import threading
import logging
from threading import Thread


logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s: %(message)s',
)

def countdown(n, number):
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


def main():
    # Thread(target=worker, name='de8ug-thread').start()
    thread_list = []
    logging.debug('start...')
    for i in range(3):
        t = Thread(target=countdown, args=(3, i+1))
        t.start()
        thread_list.append(t)
        # t.join()  # Wait until the thread terminates.
    
    for i in thread_list:
        i.join()

    logging.debug('end.')

    
if __name__ == '__main__':
    main()