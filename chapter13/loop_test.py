import asyncio
import requests
import aiohttp
from selectors import EVENT_READ
from types import coroutine

async def download(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_url(url):
    print('enter')
    async with aiohttp.ClientSession() as session:
        status = await download(session, url)
        # print('exit')
        # print(status)
        print('download complete')

def get_resource(url):
    yield url, EVENT_READ

def get_url2(url):
    html = requests.get(url)
    text = html.text
    print(text)
    print(html.status_code)

import time
if __name__ == '__main__':
    start = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [get_url('http://www.baidu.com') for i in range(10)]
    # print(tasks)
    for i in range(10):
        get_url2('http://www.baidu.com')
    # loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)