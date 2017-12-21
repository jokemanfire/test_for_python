import os 
from multiprocessing import Process
import time

def run_name(name):
    print("%s is %s" %(name,os.getpid()))

if __name__ == '__main__':
    print("parent pid is %s" % os.getpid())
    start= time.time()
    for i in range(5):
        p = Process(target= run_name, args = ["test"])
        print("child's process will start ")
        p.start()
        p.join()# 等待子进程结束再向下执行。
        print("child's process end")
    end = time.time()
    p.join()
    print(end-start)