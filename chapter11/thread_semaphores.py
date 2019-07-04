from threading import Semaphore
import threading
import time
#控制进程数量  -> Condition的应用之一
#Queue 也是 condition的应用之一

class Html(threading.Thread):
    def __init__(self, sem):
        super().__init__(name='html')
        self.sem = sem
    def run(self):
        time.sleep(2)
        print('html get...')
        self.sem.release()

class Spider(threading.Thread):
    def __init__(self, sem):
        super().__init__(name='spider')
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = Html(self.sem)
            html_thread.start()

if __name__ == '__main__':
    sem = Semaphore(3)
    spider_thread = Spider(sem)
    spider_thread.start()

