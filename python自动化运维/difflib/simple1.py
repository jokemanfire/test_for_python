# -*- coding:utf-8 -*-

import difflib

text1 = """ Not sure which exam to take? Try our online test to find out which Cambridge English exam is right for you. It’s quick, free and gives an """
text2 = """ Not sura which exam to take? Try our online test to find out which Cambridge English exam is right for you. It’s quick, free and gives a """

text_line1 = text1.splitlines()

text_line2 = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text_line1, text_line2)

print('\n'.join(list(diff)))
