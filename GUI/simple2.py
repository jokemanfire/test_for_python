from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
import sys

class App(object):

    def __init__(self,master):
        self.master = master
        self.get_top()
        self.get_buttom()

    def get_top(self):
        self.top_frame = tk.LabelFrame(self.master)
        self.top_frame.pack(ipadx = 150)
        self.first_lable = tk.Label(self.top_frame)
        self.first_lable["text"] = "欢迎登录"
        self.first_lable["font"] = (None, 30, )
        self.first_lable["fg"] = "red"
        self.first_lable["bg"] = "yellow"
        self.first_lable.pack()


    def get_buttom(self):
        self.buttom_frame =  tk.LabelFrame(self.master)
        self.buttom_frame.pack(ipadx = 70 ,pady = 40)
        self.name_lable = tk.Label(self.buttom_frame)
        self.name_lable["text"] = "用户名："
        self.name_lable["font"] = (None, 15, )
        self.name_lable.grid(row = 1, column = 1)
        self.name_get = tk.Entry(self.buttom_frame)
        self.name_get.grid(row = 1, column = 2)
        self.password_get = tk.Entry(self.buttom_frame,show ="?")
        self.password_lable = tk.Label(self.buttom_frame)
        self.password_lable["text"] = "密码："
        self.password_lable["font"] = (None, 15, )
        self.password_lable.grid(row =2, column = 1)
        self.password_get.grid(row = 2, column = 2)
        self.check_lable = tk.Label(self.buttom_frame)
        self.check_lable["text"] = "记住密码"
        self.check_button = tk.Checkbutton(self.buttom_frame)
        self.check_button.grid(row = 3, column = 2, sticky = "e")
        self.check_lable.grid(row = 3, column = 3,sticky ="w")
        self.login_button = tk.Button(self.buttom_frame, text ="登录", font= (None,15, ), command = self.message_get)
        self.login_button.grid(row = 4 , column = 2)

    def message_get(self):
        name = self.name_get.get()
        password = self.password_get.get()
        if name != "hu":
            self.error_lable(1)
        elif password != "1":
            self.error_lable(2)
        else:
            self.main_wind()

    def error_lable(self,less):
        if less == 1:
            messagebox.showinfo('错误信息', '用户名错误')
        if less == 2:
            messagebox.showinfo('错误信息', '密码错误')

    def main_wind(self):
        sys.exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("test")
    root.minsize(300,250)
    root.maxsize(300,250)
    App(root)
    root.mainloop()

