'''
a=int(input('get the value: '))
b=input('get the vaue: ')
if(a>=18):
    print('you are eligible to vote')
    if(b=="myd"):
        print('you are eligible to vote')
    else:
        print('you are non eligible to vote')
else:
    print('you are under 18')
    
a=int(input('get the value: '))
b=input('get the value: ')
if(a>=18):
    print('you are eligible to vote')
elif(b=="myd"):
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')

n=int(input('enter the value: '))
if(n%2==0):
    print('it is even')
else:
    print('it is odd')

a=9
if(a>5 and a<=10):
    print('hello')
else:
    print('bye')

amount=0
nu=int(input('enter the electricity unit: '))
if(nu<=100):
    amount=0
if(nu>100 and nu<=200):
    amount=(nu-100)*5
if(nu>200):
    amount=500+(nu-200)*10
print('amount to pay: ',amount)

n=int(input('enter the value: '))
print('last digit: ',n%10)

n=int(input('enter the value: '))
ld=n%10
if(ld%3==0):
    print('div by 3')
else:
    print('non div by 3')
    
import calendar
yy=2024
mm=6
date=3
print(calendar.month(yy,mm))
'''
m1=95
m2=80
m3=60
tot=m1+m2+m3
avg=tot/5
if(avg>90):
    print('grade a')
if(avg>80 and avg<=90):
    print('grade b')
if(avg>=60 and avg<=80):
    print('grade c')
else:
    print('grade d')
   
