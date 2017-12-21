import hashlib
#md5摘要算法
md5 = hashlib.md5()
str1 = "test"
md5.update(str1.encode("ascii"))
print(md5.hexdigest())
md5.update(str1.encode("utf-8"))
print(md5.hexdigest())
print(len(md5.hexdigest()))
#sha1摘要算法
sha = hashlib.sha1()
sha.update(str1.encode("ascii"))
print(sha.hexdigest())
sha.update(str1.encode("utf-8"))
print(sha.hexdigest())
print(len(sha.hexdigest()))