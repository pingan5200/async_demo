from multiprocessing import Process
import math


r_list = [1, 3, 5, 6, 8, 19, 20]


def circle_area(r):
    """圆形面积：pi * R * R """
    print(f'{r}: {math.pi * r * r}')
    return math.pi * r * r


def main():
    p_list = []
    for r in r_list:
        p = Process(target=circle_area, args=(r,))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

if __name__ == '__main__':
    main()

