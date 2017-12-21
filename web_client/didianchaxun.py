# -*- coding:utf-8 -*-
# 使用百度API查询吃饭地点


from urllib.request import urlopen
from urllib.parse import quote
import json

def APIlink(link):
    APIresult = urlopen(link).read()
    return APIresult

def main():
    link = "http://api.map.baidu.com/place/v2/search?"
    link3 = "http://api.map.baidu.com/place/v2/suggestion?"
    print("该脚本查询所想查找的地点")    
    region = input ("想要查询的地点，例如重庆:")
    print("你可以选择你想查询的种类和地点关键字")
    print("种类请输入'1',关键字请输入‘2’:",end = '')
    h = input("")
    h = str(h)
    if h == '2':
        query = input("地点关键字，例如“南坪”：")
        link3 = link3 + 'query=' + quote(query) + '&region=' + quote(region)+'&city_limit=true&output=json&ak=Mh1B541b7aRy9RumVsnl4Tylq9gTnveE'
        return link3
    else:
        q = input("种类关键字，例如“铁板烧”,“汽车站银行”:")
        link2 = link + 'q=' + quote(q) + '&region=' + quote(region)+ '&output=json&ak=Mh1B541b7aRy9RumVsnl4Tylq9gTnveE'
        return link2

def deal():
    message = json.loads(APIlink(main()))
    little = message.get("results")
    if little is not None:
        for key in little:
            print("名字:",key["name"],"地点:",key["address"])
    else:
        little2 = message.get("result")
        for key in little2:
            print("名字",key["name"],"地点",key["city"],key["district"])

if __name__=='__main__':
    deal()
