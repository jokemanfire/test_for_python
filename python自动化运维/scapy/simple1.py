#! C:/Python27/python2
# -*- coding:utf-8 -*-

import os, sys, time, subprocess
import warnings, logging
from scapy.all import traceroute
warnings.filterwarnings("ignore", category=DeprecationWarning) #屏蔽scapy无用警告词
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) #屏蔽IPv6多余警告词


domains = raw_input("please input one or more IP/domains:")
target = domains.split(' ')
dport = [80]

if len(target) >= 1 and target[0] != '':
    res,unans = traceroute(target,dport=dport, retry=-2)
    res.graph(target = "> test.svg")
    time.sleep(1)
    subprocess.Popen("test.svg test.png", shell=True)# svg转化为png

else:
    print  "IP/domain number of errors,exit"

