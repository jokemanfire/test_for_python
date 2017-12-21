# -*- coding:utf-8 -*-

import psutil
from subprocess import PIPE

p = psutil.Popen(['C:/Program Files (x86)/Google/Chrome/Application/chrome.exe','-c','www.baidu.com'], stdout=PIPE)
print(p.name())
print(p.username())
print(p.communicate())
print(p.cpu_times())
