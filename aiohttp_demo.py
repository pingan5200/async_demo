# async crawler demo using aiohttp
# using Python 3.6+
# by de8ug
# tips for processes:
# - http://devdocs.io/python~3.6/library/asyncio-eventloop#asyncio.AbstractEventLoop.run_in_executor
# - https://github.com/jreese/aiomultiprocess

import time
import os
import random
import string
import asyncio
import logging

import requests
import aiohttp

from timeit import DecoTime


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-10s: %(message)s',
)

BASE_DIR = r"C:\Users\sothi\Desktop\py2018\03-web\async_demo"
DOWNLOAD_DIR = os.path.join(BASE_DIR, "download")

TEST_URLS = [
    'https://source.unsplash.com/random',
    'https://source.unsplash.com/user/erondu/1600x900',
    'http://via.placeholder.com/350x150',
    'http://via.placeholder.com/350x150/1c2b3c/999'
]


def fetch_url():
    return TEST_URLS


def make_temp_name(count=5, f='.jpg'):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(count)]) + f


def download_image(url):
    try:
        r = requests.get(url).content
        logging.debug(f'get image with {url}')
        if r:
            save_file(os.path.join(DOWNLOAD_DIR, make_temp_name()), r) 
    except Exception as e:
        print(e)


def save_file(filename, data):
    logging.debug(f'saving file {filename}')
    with open(filename, 'wb') as f:
        f.write(data)


def afetch_url():
    return TEST_URLS


async def adownload_image(url, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as resp:
            filename = os.path.join(DOWNLOAD_DIR, make_temp_name(f='-a.jpg'))
            with open(filename, 'wb') as f:
                while True:
                    block = await resp.content.read(1024)
                    if not block:
                        break
                    f.write(block)


def asave_file():
    pass


async def acrawler(loop):
    logging.debug('starting async crawler...')
    urls = afetch_url()
    tasks = [adownload_image(url, loop) for url in urls]
    await asyncio.gather(*tasks)


@DecoTime()
def run_async_crawler():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(acrawler(loop))


@DecoTime()
def crawler():
    logging.debug('starting crawler...')
    urls = fetch_url()
    for url in urls:
        logging.debug(f'start downling: {url}')
        download_image(url)
    logging.debug('finish crawler.')
    

def main():
    crawler()
    run_async_crawler()

if __name__ == '__main__':
    main()