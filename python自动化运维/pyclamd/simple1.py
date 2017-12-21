# -*- coding:utf-8 -*-
#! /usr/bin/python2

from  threading import Thread
import time
import pyclamd

class Scan(Thread):

    def __init__(self,IP,scan_type,file):
        Thread.__init__(self)
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.message = ""
        self.scanresult = ""

    def run():
        try:
            i = pyclamd.ClamdNetworkSocket(IP,3310)
            if i.ping():
                self.message = self.IP + " connection ok"
                i.reload()
                if self.scan_type = "contscan_file":
                    self.scanresult = "{0}\n".format(i.contscan_file)
                elif self.scan_type = "multiscan_file":
                    self.scanresult = "{0}\n".format(i.multiscan_file)
                elif self.scan_type = "scan_file":
                    self.scanresult = "{0}\n".format(i.scan_file)
            else:
                self.message = self.IP + " connection error"
                return
        except Exception, e:
            self.message = self.IP + str(e)




def main():
    scanlist = []
    file =  "/home/ubuntu/"
    scan_type = "multiscan_file"
    IPs = ['123.206.129.82']
    threadnum = 2
    i = 1
    for ip in IPs:
        mem = Scan(ip,scan_type, file)
        scanlist.append(mem)
        if i%threadnum == 0


if __name__  == "__main__":
    main()
