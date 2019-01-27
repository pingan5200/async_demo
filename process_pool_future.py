# http://devdocs.io/python~3.6/library/concurrent.futures
from concurrent.futures import ProcessPoolExecutor

from multiprocessing import Process, Pool, get_logger, log_to_stderr
import math
import logging
import time

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(threadName)-10s: %(message)s',
# )

r_list = [1, 3, 5, 6, 8, 19, 20]


def circle_area(r):
    """圆形面积：pi * R * R """
    logging.debug(f'{r}: {math.pi * r * r}')
    return math.pi * r * r


def get_area_multi_processes():
    result_list = []
    logging.debug('multi process...')

    start = time.time()
    with ProcessPoolExecutor() as executor:
        # r: area
        # zip:  k -> v
        for r, area in zip(r_list, executor.map(circle_area, r_list)):
            print(f'{r}: {area}')

    print('multi processes time: ', (time.time() - start) * 1000)


def get_area_one_process():
    p_list = []
    logging.debug('one process...')

    start = time.time()
    for r, area in zip(r_list, map(circle_area, r_list)):
        print(f'{r}: {area}')

    print('one processes time: ', (time.time() - start) * 1000)


def main():
    # log_to_stderr()
    # get_logger()
    get_area_multi_processes()
    get_area_one_process()


if __name__ == '__main__':
    main()

