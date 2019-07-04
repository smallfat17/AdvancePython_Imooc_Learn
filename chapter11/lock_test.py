import threading
from threading import Lock,RLock

#Rlock 可以允许在一个进程内同时调用多个acquire, 但是release次数要与acquire一致

lock = RLock()
total = 0

def func1():
    global lock
    global total
    for i in range(10000):
        lock.acquire()
        total += 1
        lock.release()


def func2():
    global lock
    global total
    for i in range(10000):
        lock.acquire()
        func3()
        total -= 1
        lock.release()

def func3():
    global lock
    lock.acquire()

    lock.release()

if __name__ == '__main__':
    thread1 = threading.Thread(target=func1)
    thread2 = threading.Thread(target=func2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)

