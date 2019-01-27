import time
from queue import Queue
from threading import Thread
import requests


q_result = Queue()
urls = [
    "http://baidu.com",
    "http://qq.com",
    "http://360.com",
    "http://baidu.com",
    "http://qq.com",
    "http://360.com",
    "http://baidu.com",
    "http://qq.com",
    "http://360.com"
]


def get_page(url, queue):
    result = requests.get(url).content
    queue.put(result[:10])
    with open('url.txt', 'ab') as f:
        f.write(result[:100])


def with_thread():
    thread_list = []
    start = time.time()
    for s in urls:
        t = Thread(target=get_page, args=(s, q_result))
        t.start()
        thread_list.append(t)

    for i in thread_list:
        i.join()

    print('with thread: ', (time.time() - start) * 1000)

    return [q_result.get() for _ in range(len(urls))]


def no_thread():
    start = time.time()
    q = Queue()
    for s in urls:
        get_page(s, q)

    print('no thread: ', (time.time() - start) * 1000)

    return [q.get() for _ in range(len(urls))]


def main():
    print(no_thread())
    print(with_thread())

if __name__ == '__main__':
    main()
