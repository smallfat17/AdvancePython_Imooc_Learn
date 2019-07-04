import asyncio


async def test(raw_data):
    '''
    简单的异步非阻塞实现方式, await 后接需要异步io操作的程序或者异步函数
    :return:
    '''
    print('start...')
    data = await get_data(raw_data)
    print('finished...',str(data))

async def get_data(num):
    await asyncio.sleep(2)
    return num**2

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(20)]
    loop.run_until_complete(asyncio.wait(tasks))
