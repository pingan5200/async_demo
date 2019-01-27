# http://devdocs.io/python~3.6/library/concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import requests

urls = [
    "http://baidu.com",
    "https://www.qq.com/",
    "http://360.com",
    "http://www.51cto.com/",
    "http://web.jobbole.com/",
    "http://www.cnblogs.com/",
    "https://placeholder.com/",
    "https://www.sass.hk/",
    "https://doc.d2admin.fairyever.com/"
]


logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s: %(message)s',
)


def download(url):
    r = requests.get(url)
    return url, r.status_code


def main():
    with ThreadPoolExecutor(5, thread_name_prefix='de8ug') as executor:
        # futures = [executor.submit(download, url) for url in urls]
        # for future in as_completed(futures):
        futures_results = executor.map(download, urls, timeout=30)
        print(futures_results)
        for future in futures_results:
            try:
                # print(future.result())
                logging.info(future)
                # print(future)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()