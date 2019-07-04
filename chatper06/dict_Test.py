from collections import UserDict,defaultdict

class my_dict(UserDict):
    def __setitem__(self, key, value):
        return super().__setitem__(key, value*2)

d = my_dict()
d['one'] = 1
print(d)