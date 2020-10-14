#/usr/bin/python
#encoding=utf-8

# python socket demo
# created by joke on 2020.10.14

# reference https://docs.python.org/zh-cn/2.7/library/socket.html
	
import socket

HOST = '10.10.10.2'                 # Symbolic name meaning all available interfaces
PORT = 8077              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()	

	
