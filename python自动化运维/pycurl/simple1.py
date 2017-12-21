#! C:/Python27/python2.exe
# -*- coding:utf-8 -*-

import os,sys
import pycurl
import time

URL = "http://www.baidu.com"
c = pycurl.Curl() #创建Curl对象
c.setopt(pycurl.URL, URL) #定义请求的URL常量
c.setopt(pycurl.CONNECTTIMEOUT,  10) #定义请求链接的等待时间
c.setopt(pycurl.TIMEOUT, 10) #定义请求超时时间
c.setopt(pycurl.FORBID_REUSE, 1)  #完成交互后强制断开连接
indexfile = open("content.txt","wb")
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()
except Exception, e:
    print "error: %s" %e
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLODA = c.getinfo(c.SIZE_DOWNLODA)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print " HTTP状态码：%s" % HTTP_CODE
print "DNS解析时间 %.2f" % NAMELOOKUP_TIME*1000
print "建立连接时间 %.2f" % CONNECT_TIME*1000
print " 准备传输时间%.2f" % PRETRANSFER_TIME*1000
print "传输开始时间%.2f" % STARTTRANSFER_TIME
print " 传输总时间%.2f" % TOTAL_TIME
print " 下载数据包大小%d" % SIZE_DOWNLODA
print "HTTP头部大小%d " % HEADER_SIZE
print " 平均下载速度%d" % SPEED_DOWNLOAD

indexfile.close()
c.close()
