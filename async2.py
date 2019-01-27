import time
import asyncio
import inspect


def todo(a):
    result = yield a
    print(a + ' is doing...')
    return result + ' is done.'


async def atodo(a):
    result = a
    print(a + ' is doing...')
    time.sleep(1)
    return result + ' is done.'


def doing(x):
    result = yield todo(x)
    print(result)


# @asyncio.coroutine
async def doing_from(x):
    # result = yield from todo(x)
    # result = await todo(x)
    result = await atodo(x)
    return result


def main():
    print('doing_from: ', inspect.iscoroutinefunction(doing_from))
    print('doing_from: ', inspect.isgeneratorfunction(doing_from))
    # try:
    #     # g = doing('python')
    #     g = doing_from('python')
    #     g.send(None)
    #     g.send('python')
    # except StopIteration:
    #     pass
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(doing_from('python'))
        print(result)
    finally:
        loop.close()


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


def main_sum():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()

if __name__ == '__main__':
    # main()
    main_sum()