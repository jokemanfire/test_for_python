from urllib import request

r = request.urlopen("http://www.baidu.com")
data = r.read()
print("status ", r.status, r.reason)
for k in r.getheaders():
    print(k)

