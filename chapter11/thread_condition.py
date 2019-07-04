import threading
#condition测试

class CountOdd(threading.Thread):
    def __init__(self, cond, odd_list):
        super().__init__(name = 'odd')
        self.cond = cond
        self.odd_list = odd_list

    def run(self):
        with self.cond:
            for odd in self.odd_list:
                self.cond.wait()
                print(self.name,odd)
                self.cond.notify()


class CountEven(threading.Thread):
    def __init__(self, cond, even_list):
        super().__init__(name = 'even')
        self.cond = cond
        self.even_list = even_list

    def run(self):
        with self.cond:
            for even in self.even_list:
                self.cond.notify()
                print(self.name,even)
                self.cond.wait()


if __name__ == '__main__':
    cond = threading.Condition()

    odd_list = [i for i in range(20) if i % 2 == 1]
    even_list = [i for i in range(20) if i % 2 == 0]

    odd = CountOdd(cond,odd_list)
    even = CountEven(cond,even_list)

    odd.start()
    even.start()
