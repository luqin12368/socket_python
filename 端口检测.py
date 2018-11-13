import socket
import threading

def checkPort(address, port):
    s = socket.socket()
    try:
        s.connect((address, port))
        print('Your {} is not use.'.format(port))
        return True
    except:
        print('Your {} is used.'.format(port))
        return False

l = []

for i in range(1, 1024):
    if checkPort('172.25.9.200', i):
        l.append(i)
print('Your not use port are: ', l)
