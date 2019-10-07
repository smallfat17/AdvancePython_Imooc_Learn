#高并发爬虫
import asyncio
import os

import aiohttp
import aiomysql
from lxml import etree


start_url = 'http://www.baidu.com'
waiting_urls = []
parsed_urls = set()
STOP = False

loop = asyncio.get_event_loop()

async def fetch(url, pool):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            html = await resp.text()
            # print(html)
            parsed_urls.add(url)
            asyncio.ensure_future(parse_html(html, pool))

async def parse_html(html, pool):
    tree = etree.HTML(html)
    a_tags = tree.xpath('//a')
    if a_tags:
        for a in a_tags:
            a_url = a.attrib.get('href')
            if a_url not in parsed_urls and a_url.startswith('http'):
                print(a_url)
                waiting_urls.append(a_url)
    title = tree.xpath('//title/text()')[0]
    if title:
        asyncio.ensure_future(add_to_mysql(title, pool))


async def add_to_mysql(data, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            print(data)
            sql = "insert into blog_title(title) values('{}')".format(data)
            await cursor.execute(sql)

# async def extract_url(html):
#     pass

async def comsumer(pool):
    async with aiohttp.ClientSession() as session:
        while not STOP:
            if len(waiting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waiting_urls.pop()
            print(url,'start ..')
            asyncio.ensure_future(fetch(url, pool))
            await asyncio.sleep(0.5)

async def init_spider(pool):
    await fetch(start_url, pool)

async def main():
    pool = await aiomysql.create_pool(host='localhost', user='smallfat', password=os.getenv('MYSQL_USER_PASSWORD'), db='aio_spider', port=3306, charset='utf8', autocommit=True)
    asyncio.ensure_future(init_spider(pool))
    asyncio.ensure_future(comsumer(pool))

if __name__ == '__main__':
    loop.run_until_complete(main())
    loop.run_forever()

