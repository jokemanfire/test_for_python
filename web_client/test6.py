# -*- encoding:utf-8 -*-
import requests
import time

def crawl(url):
    try:
        key = "192.10.169.1"
        r = requests.get(url,params = key)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print("error")

if __name__ == "__main__":
    url = "http://www.baidu.com"
    t1 = time.time()
    for i in range(100):
        crawl(url)
    t2 = time.time()
    print(t2-t1)
