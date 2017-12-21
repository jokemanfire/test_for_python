# -*- coding:utf-8 -*-

import paramiko

hostname = '123.206.129.82'
username = 'ubuntu'
password = 'a123456'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname=hostname,username=username,password=password)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()