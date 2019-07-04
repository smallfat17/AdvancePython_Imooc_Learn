import asyncio, aiohttp


#简单的协程爬虫代码
async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            html = await res.text()
            return html

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    urls = ['http://www.baidu.com', 'http://www.baidu.com']
    tasks = [asyncio.ensure_future(get_html(url)) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print(task.result())



