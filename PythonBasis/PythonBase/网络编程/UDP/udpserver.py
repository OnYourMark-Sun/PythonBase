import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.1.152',9999))
print('Bind UDP on 999...')
while True:
    data,addr = s.recvfrom(1024)
    print('Received from ,',addr)
    s.sendto(b'Hello'+data,addr)
