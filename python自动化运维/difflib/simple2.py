# -*- coding:utf-8 -*-

import difflib
import os

text1 = """ Not sure which exam to take? Try our online test to find out which Cambridge English exam is right for you. It’s quick, free and gives an """
text2 = """ Not sura which exam to take? Try our online test to find out which Cambridge English exam is right for you. It’s quick, free and gives a """

text_line1 = text1.splitlines()

text_line2 = text2.splitlines()

d = difflib.HtmlDiff()
dff =  d.make_file(text_line2, text_line1)
with open("test.html","w") as f:
    for i in dff:
        f.write(i)

