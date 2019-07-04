import time

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED, ProcessPoolExecutor
from concurrent.futures import Future


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib2(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a+b
    return a
if __name__ == '__main__':
    threadpool = ProcessPoolExecutor(max_workers=3)
    start_time  = time.time()
    all_task = [threadpool.submit(fib,(n)) for n in range(25,40)]
    for task in as_completed(all_task):
        print(task.result())
    print('total_time: ', time.time() - start_time)

#ThreadPool
#total_time:  61.86245131492615
#total_time:  0.0010042190551757812

#ProcessPoll
#total_time:  28.366820096969604
#total_time:  0.08021306991577148