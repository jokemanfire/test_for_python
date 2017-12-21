#! -*- coding:utf-8 -*-

import os
#os文件操作
k = os.path.abspath("")#当前文件目录路径
m = os.path.join(k,"test")
print(m)
os.mkdir(m)
os.rmdir(m)


for i in os.listdir(os.path.abspath("")):#取出所有py文件
    if str(os.path.splitext(i)[1]) == ".py":
        print(i)