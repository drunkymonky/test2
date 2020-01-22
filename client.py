import socket
from pydoc import cli

HOST = 'localhost'
PORT = 12344

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(bytes('Hello'.encode('utf-8'))) #byte()
    data = client.recv(1024)
    print(data)





