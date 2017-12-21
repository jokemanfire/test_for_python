import subprocess

p = subprocess.Popen(["nslookup"], stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr= subprocess.PIPE  )
t = p.communicate("baidu.com\n exit\n")
print (t)

