import socket 
import threading 

import time



class Server_Listen(object):
    def __init__ (self,client):
        self.client = client
        self.message_get()



    def message_get(self):
        while True:
            self.message = self.client.recv(1024)
            print(self.message)
            if self.message is not None:
                message_send(self.client,self.message)


def sock_create(s):
    while True:
        sock, addr = s.accept()
        print(sock)
        if sock:
            all_client.append(sock)
            t = threading.Thread(target = Server_Listen ,args = [sock] )
            t.start()

def message_send(myself,message): 
    for client in all_client:
        client.send( b"yes")
        if client != myself:
            client.send(message)

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",8080))
    s.listen(5)
    sock_create(s) 


if __name__ == "__main__":
    all_client = []
    main()
