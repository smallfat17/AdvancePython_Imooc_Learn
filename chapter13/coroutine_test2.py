import time
import asyncio
import random

async def compute(x, y):
    print('%d + %d counting...' % (x, y))
    with open('1.txt', 'a', encoding='utf8') as f:
        await write(f, str(x + y))
    return x + y

async def write(f, data):
    f.write(data + '\n')
    f.flush()

async def print_sum(x, y):
    result = await compute(x, y)
    print('%d + %d = %d' %(x,y,result))

def count_write(x, y):
    print('%d + %d is countin...' % (x, y))
    with open('2.txt', 'a', encoding='utf8') as f:
        f.write(str(x + y) + '\n')
    print('%d + %d = %d' % (x , y ,x + y ))
    return x + y

if __name__ == '__main__':
    import time
    start = time.time()

    #68.583744764328
    # loop = asyncio.get_event_loop()
    # tasks = []
    # for i in range(20000):
    #     tasks.append(print_sum(random.randint(1000000, 2000000), random.randint(10000000, 200000000)))
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()

    #82.29798769950867
    for i in range(20000):
        r = count_write(random.randint(1000000, 2000000), random.randint(10000000, 200000000))
    print(time.time() - start)