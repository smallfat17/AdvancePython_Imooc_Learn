import asyncio

async def func(sleep_times):
    print('enter')
    await asyncio.sleep(sleep_times)
    print('exit')

if __name__ == '__main__':
    task1 = func(4)
    task2 = func(3)
    task3 = func(1)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    #取消协程
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        print(len(all_tasks))
        for task in all_tasks:
            print(task)
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()