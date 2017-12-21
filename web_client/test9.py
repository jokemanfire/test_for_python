from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def cleaninput(input):
    input = re.sub('\n+'," ",input)
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +'," ",input)
    input = bytes(input,"utf-8")
    input = input.decode("ascii","ignore")
    cleaninput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleaninput.append(item)
        return cleaninput

def ngrams(input,n):
    input = cleaninput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+1])
        return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsobj = BeautifulSoup(html)
content = bsobj.find("div",{"id":"mw-content-text"}).get_text()
ngrams = ngrams(content,2)
print(ngrams)