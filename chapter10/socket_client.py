import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8001))
while True:
    data = input('data: ')
    client.send(data.encode('utf8'))
    if data == 'bye':
        break
    receive_data = client.recv(1024)
    print(receive_data.decode('utf8'))

client.close()
