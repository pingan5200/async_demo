from multiprocessing import Process, Pool
import math


r_list = [1, 3, 5, 6, 8, 19, 20]


def circle_area(r):
    """圆形面积：pi * R * R """
    print(f'{r}: {math.pi * r * r}')
    return math.pi * r * r


def main():
    p_list = []

    p = Pool(3)
    for r in r_list:
        result = p.apply_async(circle_area, args=(r, ))
        p_list.append(result)

    for p in p_list:
        print(p.get())

if __name__ == '__main__':
    main()

