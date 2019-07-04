'''
将函数的参数截取定制成新的函数
'''

from functools import partial

def func(url, callback):
    print(url)
    callback()

def callback():
    print('callback')

if __name__ == '__main__':
    newfunc = partial(func, 'http://www.baidu.com')
    newfunc(callback)
