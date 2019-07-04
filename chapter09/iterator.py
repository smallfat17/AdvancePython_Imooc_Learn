from collections.abc import Iterator

class Company:
    def __init__(self,employees):
        self.employees = employees

    def __iter__(self):
        return MyIterator(self.employees)

#自定义迭代器
class MyIterator(Iterator):
    def __init__(self,employees):
        self.employees = employees
        self.index = 0

    def __next__(self):
        try:
            word = self.employees[self.index]
        except :
            raise  StopIteration
        self.index += 1
        return word

if __name__ == '__main__':
    company = Company(['john','lilith','tom'])
    for employee in company:
        print(employee)
