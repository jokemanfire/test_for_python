# -*- encoding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='a123456',db='mysql')
cur = conn.cursor()
cur.execute("USE test2")

random.seed(datetime.datetime.now())

def store(title,content):
    cur.execute("INSERT INTO wiki(title,content) VALUES(\"%s\",\"%s\")",(title.encode('utf-8'),content.encode('utf-8')))
    cur.connection.commit()

def getlinks(articleurl):
    html = urlopen("http://en.wikipedia.org"+articleurl)
    bsobj = BeautifulSoup(html)
    title = bsobj.find("h1").get_text()
    content = bsobj.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title,content)
    return bsobj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getlinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticle)
        links = getlinks(newArticle)
finally:
    cur.close()
    conn.close()
