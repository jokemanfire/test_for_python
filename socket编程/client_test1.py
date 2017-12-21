import socket
import time
import threading
import tkinter
import sys
from tkinter import *

class My_clientGUI():
    def __init__ (self, master,sock):
        self.s = s
        self.master = master
        self.sock = sock
        self.socket_connect()     
        self.message_thread = threading.Thread(target = self.message_get)
        self.sendmessage_thread = threading.Thread(target = self.message_send)
        self.message_thread.start()
        #self.sendmessage_thread.start()
        self.up_window(all_message)
        self.send_frame() 

    def up_window(self,all_message):
        self.up_frame = tkinter.LabelFrame(self.master)
        self.up_frame.pack()
        self.first_lable = tkinter.Listbox(self.up_frame, width = 60, height = 10)
  
        #self.first_lable.insert(count,message)

        #self.first_lable.update()
        self.first_lable.pack()
        
    
    def socket_connect(self):
        try:
            self.sock.connect(("0.0.0.0",8080))
        except:
            print("connect error")
        
    def send_frame(self):
        global send_messages
        self.low_frame = tkinter.Frame(self.master)
        self.low_frame.pack()
        self.write_text = tkinter.Text(self.low_frame,width= 40, height = 5)
        self.write_text.pack()
        self.send_button = tkinter.Button(self.low_frame)
        self.send_button['text'] =  "发送"
        self.send_button['command'] = self.get_message
        self.send_button.pack()
        self.exit_button = tkinter.Button(self.low_frame)
        self.exit_button['text'] = "退出"
        self.exit_button['command'] = Frame(self.master).quit
        self.exit_button.pack()


    def message_get(self):
        #f  = open("test.txt","w")
        while True:
            self.others_message = self.sock.recv(1024)
            #f.write(self.others_message)
            if self.others_message is not None:
                self.first_lable.insert(tkinter.END, "from others" + self.others_message.decode("utf-8"))
        #f.close()     


    def message_send(self):
        #f = open("test.txt","w")
        if self.input_message is not None:    
            #f.write(self.message)   
            self.message = self.input_message.encode('utf-8')
            self.sock.send(self.message)
            #all_message.append(self.message)
        #f.close()

    def get_message(self):
        self.input_message = self.write_text.get('1.0', tkinter.END)
        global send_messages
        send_messages = self.input_message
        times = time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime())
        self.first_lable.insert(tkinter.END, '客户端 ' + times  +self.input_message )
        self.write_text.delete(0.0, self.input_message.__len__()-1.0)
        self.message_send()


def main(s):
    tk = tkinter.Tk()
    tk.title("test")
    tk.minsize(300,250)
    #tk.maxsize(300,250)
    My_clientGUI(tk,s)
    tk.mainloop()

       

if __name__  == "__main__":
    send_messages = ""
    all_message = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main(s)
