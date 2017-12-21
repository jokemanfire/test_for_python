# -*- coding:utf-8 -*-

from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import random
import datetime
import re
import os
 
pages = set()
try:
    os.mkdir('test')
except:
    pass

def getlinks(pagelink):
    global pages
    images = BeautifulSoup(urlopen(pagelink)).findAll('img')
    for image in images:
        random.seed(datetime.datetime.now())
        path = 'test/' + str(random.random()) + '.jpg'
        pink = image.attrs['src']
        print(pink)
        if os.path.isfile is not True:
            dow = urlretrieve(pink,path)
    links = BeautifulSoup(urlopen(pagelink)).findAll('a',href=re.compile('.+'))
    for link in links:
        if link.attrs['href'] not in pages:
            pages.add(link)
            try:
                getlinks(link.attrs['href'])
            except:
                pass

if __name__ == '__main__':
    html = 'http://www.mm131.com/'
    getlinks(html)
    
    
    

