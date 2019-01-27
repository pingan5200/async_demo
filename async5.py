import asyncio

async def hello_world():
    print("Hello World!")

# asyncio.run(hello_world()) # 3.7+,配合上面的hello_world运行，run是3.7里面一个新的方法，可以安装Python 3.7版本进行测试。3.7刚发布不久，等再稳定一些，课程逐渐迁移到Python 3.7


def hello_world(loop):
    print('hello world with loop')
    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)

# call_later
# loop.call_later(2, hello_world, loop)

# call_at
current = loop.time()
loop.call_at(current + 10, hello_world, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()