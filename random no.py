import random
a=random.randint(0,100)
print(a)
while(True):
    b=int(input('enter the value : '))
    if(a>b):
        print('greater than')
    elif(a<b):
        print('less than')
    elif(a==b):
        print('both are equal')
        break
