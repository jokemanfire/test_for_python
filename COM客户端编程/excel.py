import win32com.client as win32
from time import sleep
import tkinter

RANGE = range(3,8)
def excel():
    app = 'Excel'
    x1 = win32.Dispatch('Excel.Application')
    ss = x1.Workbooks.Add()
    sh = ss.ActiveSheet
    x1.Visible = True
    sleep(1)
    sh.Cells(1,1).Value = ('Python-to-%s Demo' % app)
    sleep(1)
    for i in RANGE:
        sh.Cells(i,1).Value = ('Line %d' % i)
        sleep(1)
    sh.Cells(i+2,1).Value = "Th-th-th-that's all folks!"
    sleep(1)
    ss.Close(False)
    x1.Application.Quit()

if __name__ == '__main__':
    excel()
