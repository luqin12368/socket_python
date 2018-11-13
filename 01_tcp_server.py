# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 5000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()
    with conn:
        print('Connected by', address)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(str(data, encoding='utf-8'))
            conn.sendall(data)
