import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("www.baidu.com",80))
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nUser-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nConnection: close\r\n\r\n')
while True:
    d = s.recv(1024)
    if d:
        print(d) 
    else:
        break