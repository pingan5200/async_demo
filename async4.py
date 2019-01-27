import asyncio
import time


async def write_file(filename, data):
    with open(filename, 'w') as f:
        # time.sleep(3)
        await asyncio.sleep(3)
        f.write(data)
    return f'{filename} ok'


async def work(data_list):
    coro_list = [write_file(data.split(':')[0], data) for data in data_list]
    done, pending = await asyncio.wait(coro_list)
    for d in done:
        print(d.result())


async def work_task(data_list):
    tasks = [asyncio.ensure_future(write_file(data.split(':')[0], data)) for data in data_list]
    # done, pending = await asyncio.wait(tasks)
    # for d in done:
    #     print(d.result())
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


def main():
    data_list = [
        'de8ug:writing skdjflsslakdsldjgsg',
        'lilei:doing skdjflsslakdsldjgsg',
        'hmm:playing skdjflsslakdsldjgsg',
    ]
    loop = asyncio.get_event_loop()
    try:
        print('start working...')
        start = time.time()
        # loop.run_until_complete(work(data_list))
        loop.run_until_complete(work_task(data_list))
    finally:
        loop.close()
        print('cost: ', time.time() - start)

if __name__ == '__main__':
    main()