#读取大文件
def MyReadLines(f, newline):
    buffer = ''
    while True:
        while newline in buffer:
            position = buffer.index(newline)
            yield buffer[:position]
            buffer = buffer[position + len(newline):]
        chunk = f.read(4096)
        if not chunk:
            yield buffer
            break
        buffer += chunk


with open('test.txt','r') as f:
    for line in MyReadLines(f,'||'):
        print(line)




