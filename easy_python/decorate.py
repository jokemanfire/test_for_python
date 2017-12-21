import re

def first(*mf):
    if  re.match("<(.+)>",str(*mf)) is  None:
        def bt(kw):
            print(kw.__name__)
            def third(*args):
                return kw(*args)
            return third
        return bt
    else:
        print(mf[0].__name__)
        def gbt(*wc):
            return mf[0](*wc)
        return gbt

shit = 1
@first(shit)
def second(nice):
    print(nice)

second("df")

@first
def second(nice):
    print(nice)

second("mf")