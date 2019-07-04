import time
import queue
import multiprocessing
from multiprocessing import Process, Manager, Pool, Pipe

def func1(queue, data):
    time.sleep(1)
    print('func1',data)
    queue.put(data)

def func2(queue):
    data = queue.get()
    print('func2',data)

def producer(send_pipe):
    send_pipe.send("hello, I'm producer")

def comsumer(recv_pipe):
    data = recv_pipe.recv()
    print('comsumer_recv:',data)

if __name__ == '__main__':
    #Queue
    #from queue import Queue    -> 多线程中使用
    #from multiprocessing import Queue  -> 多进程中使用
    #from multiprocessing import Manager  -> Manager().Queue() -> 进程池中使用

    #进程池
    # queue = Manager().Queue()
    # pool = Pool(2)
    # pool.apply_async(func1, args=(queue, 5))
    # pool.apply_async(func2, args=(queue,))
    # pool.close()
    # pool.join()

    #多进程
    # queue = multiprocessing.Queue()
    # process1 = Process(target=func1, args=(queue, 5))
    # process2 = Process(target=func2, args=(queue,))
    # process1.start()
    # process2.start()
    # process1.join()
    # process2.join()

    #Pipe  只适用于两个进程, 性能优于Queue
    send_pipe, recv_pipe = Pipe()
    process1 = Process(target=producer, args=(send_pipe,))
    process2 = Process(target=comsumer, args=(recv_pipe,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()