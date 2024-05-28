""" import threading
import time
def fun():
    for i in range(1,6):
        print(i)
        time.sleep(3)
thread1=threading.Thread(target=fun())
thread1.start()
thread1.join()
print("finished") """

import threading
import time
def fun():
    for i in range(1,4):
        print(i)
        time.sleep(5)
def fun1():
    for char in ['a','b','c']:
        print(char)
        time.sleep(5)
thread2=threading.Thread(target=fun)
thread1=threading.Thread(target=fun1)
thread2.start()
thread1.start()
thread2.join()
thread1.join()
print('finished')