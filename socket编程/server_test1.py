import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("172.18.62.50", 8080))
s.listen(5)


def tcplink(sock,addr):
    print("accept link from %s:%s" %addr)
    sock.send(b"welcome")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        print(data)
        if data.decode('utf-8') == "exit":
            break
        sock.send(b"hello sb")
    sock.close()
    print ("connection exit")

while True:
    sock, addr  = s.accept()
    t = threading.Thread(target=tcplink, args = [sock,addr])
    t.start()

