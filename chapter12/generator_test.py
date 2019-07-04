result = {}

def add_total(key):
    current_total = 0
    nums = []
    while True:
        x = yield
        if x is None:
            break
        print(key,x)
        current_total += x
        nums.append(x)
    return current_total, nums

def get_total(key):
    while True:
        result[key] = yield from add_total(key)
        print(key,'count success')

def main(data):
    for key, value in data.items():
        gen = get_total(key)
        gen.send(None)
        for i in value:
            gen.send(i)
        gen.send(None)
    print(result)

def gen1():
    total = 0
    while True:
        x = yield
        if x is None:
           break
        else:
            total += x
            print('x', x)

    return total

def gen2():
    while True:
        x = yield from gen1()
        print('total',x)

if __name__ == '__main__':
    data = {
        'A': [500,100,200],
        'B': [50,90,88,77,200],
        'C': [-50,800,455,66,774,80]
    }
    # main(data)

    # print()
    g = gen2()
    g.send(None)
    g.send(1)
    g.send(None)
    # g.send(5)



    # import socket
    # client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # client.connect(('10.0.113.5',8004))
    #
    # client.send(b'D\x00\x00\x00')
    #
    # client.close()