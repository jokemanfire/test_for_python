# -*-  ecoding:utf-8 -*-
#马尔科夫模型的实例

from urllib.request import urlopen
from random import randint

def wordListSum(wordlist):
    sum = 0
    for word,value in wordlist.items():
        sum += value
    return sum

def retrieveRandomWord(wordlist):
    randIndex = randint(1,wordListSum(wordlist))
    for word,value in wordlist.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildworddict(text):
    #剔除换行符和引号
    text = text.replace("\n"," ")
    text = text.replace("\""," ")
    #保证每个标点符号都和前面的单词在一起
    #这样就不会被剔除马尔科夫链
    punctuation = [',','.',';',':']
    for sysmble in punctuation:
        text = text.replace(sysmble," "+sysmble+" ")
    words = text.split(" ")
    #过滤空单词
    words = [word for word in words if word != ""]
    wordDict = {}
    for i in range(1,len(words)):
        if words[i-1] not in wordDict:
            #为单词新建一个辞典
            wordDict[words[i-1]] = {}
            if words[i] not in wordDict[words[i-1]]:
                wordDict[words[i-1]][words[i-1]] = 0
            wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1
    return wordDict

text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
wordDict = buildworddict(text)
#生成链长为100的马尔科夫链
length = 100
chain = ""
currentWord = "I"
for i in range(0,length):
    chain += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])
print(chain)