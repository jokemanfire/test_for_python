
import requests
from bs4 import BeautifulSoup
import pymysql
from urllib.request import urlopen
import re

conn = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = 'a123456',db = 'mysql')
cur = conn.cursor()
cur.execute("USE test2")
lists = set()
def deal(url):
    r = urlopen(url)
    b = BeautifulSoup(r.read())
    m = b.find("title").get_text()
    f = m.encode('utf-8','ignore')
    cur.execute("INSERT INTO jidong(content) VALUES (\"%s\")",f)
    cur.connection.commit()

def main():
    url = "http://item.jd.com/1887526.html"
    page(url)
    

def page(url):
    pages = urlopen(url)
    m = BeautifulSoup(pages.read())
    urls = m.findAll("a",href=re.compile('^(//item.jd.com/)\d+\.html'))
    for i in urls:
        print('http:' + i.attrs['href'])
        if i.attrs['href'] not in lists:
            lists.add(i.attrs['href'])
            deal('http:' + i.attrs['href'])
            page('http:' + i.attrs['href'])
        else:
            pass

if __name__=="__main__":
    main()
    conn.close()
    cur.close()


