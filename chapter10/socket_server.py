import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8001))
server.listen()

def sock_handle(sock,addr):
    while True:
        data = sock.recv(1024).decode('utf8')
        print(data)
        if data == 'bye':
            break
        sock.send('hello,client'.encode('utf8'))

while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=sock_handle,args=(sock,addr))
    client_thread.start()

server.close()
