import asyncio

def func():
    pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon(func)
    loop.call_later(4, func)
    print(loop.time())
    loop.stop()
    loop.run_forever()