import asyncio

import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://baidu.com') as resp:
            print(resp.status)
            print(await resp.text())
            # print(await resp.json())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

