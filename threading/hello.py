import os
import time
# while 1:
# 	os.system('hello.exe')
# 	time.sleep(1)


import time, threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 10:
        n = n + 1
        os.system('hello.exe')
        # print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop)
t.start()

t1 = threading.Thread(target=loop)
t1.start()

t2 = threading.Thread(target=loop)
t2.start()

t3 = threading.Thread(target=loop)
t3.start()

t3.join()
t.join()
t2.join()
t1.join()
print 'thread %s ended.' % threading.current_thread().name

