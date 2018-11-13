import socket
from threading import Thread
import sys

host = '172.25.9.200'
port = 50008


def send_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = ''
    while data != 'q':
        data = input()
        s.sendto(data.encode('utf-8'), (host, port))
    s.sendto(data.encode('utf-8'), (host, port))
    s.close()
    sys.exit()


def r_data():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1.bind((host, port))
    data = b''
    while data.decode('utf-8') != 'q':
        data, address = s1.recvfrom(1024)
        print('\ndata:', data.decode('utf-8'), '\naddress:', address)
    s1.close()
    sys.exit()


t1 = Thread(target=send_data)
t1.start()

t2 = Thread(target=r_data)
t2.start()
