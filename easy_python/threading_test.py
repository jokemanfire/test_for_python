# 锁与线程
import threading
import time

lock = threading.Lock()
def loop():
    print ("thread %s in running" % threading.current_thread().name)
    n = 0 
    lock.acquire()
    while n <5:
        n = n+1
        print("thread %s >>> %s" % (threading.current_thread().name,n ))
        time.sleep(1)
    print("thread %s ended " % threading.current_thread().name)
    lock.release()

print("thread %s ins running" %threading.current_thread().name)
for i in range (5):
    t = threading.Thread(target=loop)
    t.start()
t.join()

print("thread %s ended" % threading.current_thread().name)