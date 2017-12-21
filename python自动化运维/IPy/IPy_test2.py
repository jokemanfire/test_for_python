# -*- coding:utf-8 -*-

from IPy import IP

def IP_information(ip): 
    ips =  IP(ip)
    print('net %s'% ips.net())
    print('net mask %s' % ips.netmask())
    print('broadcast %s' % ips.broadcast())




ip = input("your ip or some")

if __name__ == '__main__':
    IP_information(ip)
