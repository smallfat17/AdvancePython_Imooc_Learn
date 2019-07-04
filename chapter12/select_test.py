import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()
stop = False
urls = []
#回调+事件循环+select/poll/epoll 模式解决高并发问题

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf8'))
        selector.register(self.client.fileno(), EVENT_READ, self.read)

    def read(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            print(self.data.decode('utf8'))
            self.client.close()
            urls.remove(self.raw_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.raw_url = url
        url = urlparse(url)
        self.data = b''
        self.host = url.netloc
        self.path = url.path
        if self.path == '':
            self.path = '/'

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except:
            pass

        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

#请求socket状态
def loop():
    #selector封装select并且提供register模式
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)

if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(20):
        urls.append('http://www.baidu.com')
        fetcher = Fetcher()
        fetcher.get_url('http://www.baidu.com')
    loop()
    print('total:',time.time() - start)

#
# def get_html(url):
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
#     if path == '':
#         path = '/'
#
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setblocking(False)
#     try:
#         client.connect((host, 80))
#     except BlockingIOError:
#         pass
#     while True:
#         try:
#             client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
#             break
#         except OSError as e:
#             pass
#
#
#     data = b''
#     while True:
#         try:
#             d = client.recv(1024)
#         except BlockingIOError as e:
#             continue
#         if d:
#             data += d
#         else:
#             break
#     print(data.decode('utf8'))




