import socket
from urllib.parse import urlparse

def crawl(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host, 80))
    print('connect success')
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode('utf8'))
    print('send request sucess')

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    print(data.decode('utf8'))
    # print(url)

if __name__ == '__main__':
    url = 'http://120.78.187.183/'
    # crawl(url)
    import requests
    from lxml import etree
    res = requests.get(url)
    tree = etree.HTML(res.text)
    print(tree.xpath('//title/text()')[0])
    # for a in tree.xpath("//a"):
    #     print(a.attrib.get('href'))
