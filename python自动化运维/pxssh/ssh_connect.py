# -*- coding:utf-8 -*-
import pxssh

def sendcommand(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before

def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print 'error'
        exit(0)

s = connect('')#链接IP
sendcommand(s, 'ls -l')
