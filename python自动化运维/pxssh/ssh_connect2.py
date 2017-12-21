# -*- coding:utf-8 -*-

import pxssh

hos = 123.206.129.82
user = ubuntun
password = hudingyang123
def send_cmd(cmd):
    try:
        s = pxssh.pxssh()
        s.login(host, user ,password)
        s.send_line(cmd)
        s.prompt()
        print s.before
    except:
        print(error)
        exit(0)

if __name__ == '__main__':
    cmd = 'ls -a'
    send_cmd(cmd)

