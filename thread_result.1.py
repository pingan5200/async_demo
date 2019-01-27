import time
from queue import Queue
from threading import Thread


# ref: https://stackoverflow.com/questions/11986005/better-way-to-get-results-from-multiple-threads


q_result = Queue()
str_list = ['222', '5555', '888', '666']  # => 222, 5555...


def str_to_int(arg, queue):
    result = int(arg)
    queue.put({arg: result})


def with_thread():
    thread_list = []
    start = time.time()
    for s in str_list:
        t = Thread(target=str_to_int, args=(s, q_result))
        t.start()
        thread_list.append(t)

    for i in thread_list:
        i.join()

    print('with thread: ', (time.time() - start) * 1000)

    # print(q_result)
    # for i in str_list:
    #     print(q_result.get())
    return [q_result.get() for _ in range(len(str_list))]


def no_thread():
    start = time.time()
    q = Queue()
    for s in str_list:
        str_to_int(s, q)

    print('on thread: ', (time.time() - start) * 1000)

    return [q.get() for _ in range(len(str_list))]


def main():
    no_thread()
    with_thread()

if __name__ == '__main__':
    print(main())
