import win32com.client as win32
from time import sleep

RANGE = (3,8)

def ppoint():
    ppoint = win32.Dispatch('Powerpoint.Application')
    pres = ppoint.Presentations.Add()
    ppoint.Visible = True
    s1 = pres.Slides.Add(1,win32.constants.ppLayoutText)
    sleep(1)
    sla = s1.Shapes[0].TextFrame.TextRange
    s1a.Text = 'python-to-powerpoint'
    sleep(1)
    s1b = s1.Shapes[1].TextFrame.TextRange
    for i in RANGE:
        s1b.InsertAfter('Line %d \r\n'% i)
        sleep(1)
    s1b.InsertAfter("\r\nwijiwew\r\n")
    pres.Close()
    ppoint.Quit()

if __name__ == '__main__':
    ppoint()
