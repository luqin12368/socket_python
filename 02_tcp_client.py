# Echo client program
import socket

HOST = '172.25.10.207'    # The remote host
PORT = 5001             # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    sent_date = input('输入想要说的话：')
    s.sendall(bytes(sent_date, encoding='utf-8'))
    data = s.recv(1024)
print('Received', str(data, encoding='utf-8'))
s.close()
