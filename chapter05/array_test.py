import array

a = array.array('i')
a.append(1)
a.append(2)
a.append(-1)

# print(a)
# print(dir(a))

class myList():
    def __init__(self,students):
        self.students = students

    def __getitem__(self, item):
        return self.students[item]

    def __str__(self):
        return ','.join(self.students)

    def __len__(self):
        return len(self.students)

l = myList(['john','mike','lilith'])

print(len(l))

#上下文管理器
class Sample:
    def __enter__(self):
        print('enter...')
        return self

    def do_something(self):
        print('do something')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit...')

with Sample() as s :
    s.do_something()


import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print('enter')
    yield {}
    print('exit')

with file_open('ff') as f:
    print(f)