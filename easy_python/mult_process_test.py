from multiprocessing import Pool
import os, time ,random

def long_time_task(name):
    print("run task %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(1)
    end = time.time()
    print (" Task %s runs time %d" % (name,end-start))

if __name__ == "__main__":
    print("parent process is %s" % os.getpid())
    p = Pool(9)
    for i in range(10):
        p.apply_async(long_time_task, args=[i])
    print("wating for all process done")
    p.close()
    p.join()
    print("all done")