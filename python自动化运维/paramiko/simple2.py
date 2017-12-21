# -*- coding:utf-8 -*-

import paramiko
import os

hostname = '123.206.129.82'
username = 'ubuntu'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey = os.path.expanduser('/home/hu/my_keys.txt')
key = paramiko.RSAKey.from_private_key_file(privatekey)

ssh.connect(hostname=hostname, username=username, pkey= key)
stdout = ssh.exec_command('free -m')
print stdout[1].read()
ssh.close()