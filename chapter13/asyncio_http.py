import socket
import asyncio
import time
from urllib.parse import urlparse

#asynicio 底层接口实现http请求

async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    all_lines = []
    async for line in reader:
        line = line.decode('utf8')
        all_lines.append(line)
    html = '\n'.join(all_lines)
    print(html)
    return html

async def main():
    tasks = []
    for i in range(20):
        tasks.append(asyncio.ensure_future(get_url('http://www.baidu.com')))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_url('http://www.baidu.com'))
    loop.run_until_complete(main())
    loop.close()