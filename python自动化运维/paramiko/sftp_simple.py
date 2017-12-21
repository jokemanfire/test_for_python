# -*- coding:utf-8 -*-

import paramiko

username = 'ubuntu'
password = 'hudingyang123'
hostname = '123.206.129.82'
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put("")
    sftp.get("")
    sftp.mkdir("")
    sftp.rmdir("")
    sftp.rename(",")
    print sftp.stat("")
    print sftp.listdir("")
    t.close()

except Exception, e:
    print str(e)