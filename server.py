import socket

HOST = 'localhost'
PORT = 12344

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    conn, addr = server.accept()
    while True:
        print(conn)
        print(addr)
        data = conn.recv(1024)
        print(data)
        decode_data = data.decode('utf-8')
        conn.sendall(data)


