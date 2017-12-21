# -*- encoding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='a123456',db='mysql')
cur = conn.cursor()
cur.execute("USE test2")
page = set()
def main(url):
    global page
    r = BeautifulSoup(requests.get(url).text)
    url = r.findAll('a',href=re.compile('^(http).+'))
    for i in url:
        url = i.attrs['href']       
        cur.execute("INSERT INTO unimportant(url) VALUES(\"%s\")",url)
        cur.connection.commit()
        getlinks(url)

def getlinks(url):
    if url not in page:
        page.add(url)
        print(url)
        main(url)
    else:
        pass

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Wiki'
    main(url)
    conn.close()
    cur.close()
    

    
   
