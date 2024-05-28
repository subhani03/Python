import threading
def f1():
    for i in range(1,4):
        print(i)
def f2():
    x=['orange','apple','mango']
    for i in x:
        print(i)
def f3():
    for char in ['a','e','i','o','u']:
        print(char)
def f4():
    for animal in ['panda','cat']:
        print(animal)
def f5():
    for ic in ['chocobar','butterscotch']:
        print(ic)


thread1=threading.Thread(target=f1)
thread2=threading.Thread(target=f2)
thread3=threading.Thread(target=f3)
thread4=threading.Thread(target=f4)
thread5=threading.Thread(target=f5)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
print('thread are ended')

