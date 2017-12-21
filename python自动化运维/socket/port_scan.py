# -*- coding:utf-8 -*-

import socket
import threading

def port_scan(host, port):
    socket.setdefaulttimeout(1)
    try:
        f = socket(AF_INET, SOKC_STREAM)
        f.connect(host, port)
        print("host:port%s"%f.recv(1024))
    except:
        pass
    num.release()

host = '45.77.27.155'
port = 2000
num = threading.Semaphore(1000)


if __name__ == '__main__':
    for i in range(1,10000):
        print(i)
        t = threading.Thread(target = port_scan, args = (host, i ))
        t.start()
    
