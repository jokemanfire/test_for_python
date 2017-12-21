# -*- coding:utf-8 -*-
# python2.7

import sys
import nmap

scan_row = []
input_data = raw_input('Please input hosts and port: ')
scan_row = input_data.split(" ")
if len(scan_row) != 2:
    print " input errors,example \"192.168.1.0/24 80,443,22\""
    sys.exit(0)
hosts = scan_row[0]
port = scan_row[1]

try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('nmap not find', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpect error")
    sys.exit(0)

try:
    nm.scan(hosts = hosts, arguments = ' -v -sS -p '+port)
except Exception,e:
    print "scan erro"+str(e)

for host in nm.all_hosts():
    print('----------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print(' state : %s' % nm[host].state())
    for po in nm[host].all_protocols():
        print('------------------')
        print("Protocol :%s" % po)

        lport = nm[host][po].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate :%s'% (port, nm[host][po][port]['state']))
