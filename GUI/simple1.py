import tkinter as tk
import tkinter.messagebox as messagebox

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nameInput = tk.Entry(self)
        self.nameInput.pack()
        self.button = tk.Button(self)
        self.button['text'] = "hello"
        self.button['command'] = self.say_hi
        self.button.pack()

    def say_hi(self):
        name = self.nameInput.get() or "world"
        messagebox.showinfo('Message','hello,%s' %name)

app = Application()
app.master.title("hello world")
app.master.minsize(250,50)
app.mainloop()