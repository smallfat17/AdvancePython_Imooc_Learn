def callback():
    print('this is callback')

def test(fn):
    print('xixixi')
    fn()

def test2():
    try:
        print('try..')
        return ('ok')
    finally:
        print('finally')

if __name__ == '__main__':
    test(callback)
    print(test2())