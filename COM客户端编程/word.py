import win32com.client as win32
from time import sleep

RANGE = (3,8)

def word():
    word = win32.Dispatch('Word.Application')
    doc = word.Documents.Add()#添加文档
    word.Visible = True#可见
    sleep(1)
    rng = doc.Range(0,0)
    rng.InsertAfter('python-to-word\r\n')
    sleep(1)
    for i in RANGE:
        rng.InsertAfter('Line %d\r\n'%i)
        sleep(1)
    rng.InsertAfter("\r\nwdnjwdiw\r\n")
    doc.Close(False)#退出不保存
    word.Application.Quit()

if __name__ == '__main__':
    word()
