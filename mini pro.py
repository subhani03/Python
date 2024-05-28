print('1.adam,2.armstrong,3.fact,4.fibonacci,5.palindrome')
i=int(input('enter the no: '))
if(i==1):
    print('adam no')
n=int(input('enter the value: '))
n1=n*n
r=0
while(n>0):
    a=n%10
    r=(r*10)+a
    n=n//10
    b=r*r
c=0
while(n>0):
    a=b%10
    c=(c*10)+a
    b=b//10
if(n1==c):
    print('adam no')

elif(i==2):
    print('armstrong')
    n=int(input('enter the value: '))
    r=0
    while(n>0):
        a=n%10
        r=r+(a*a*a)
        n=n//10
        print(r)
elif(i==3):
    print('fact')
n=int(input('enter the value: '))
fact=1
while(n>0):
    fact=fact*n
    i-=1
    print('fact no: ',fact)
elif(i==4):
    print('fibonacci')
n=int(input('enter the value: '))
x=1
y=1
while(i>=1):
    z=x+y
    print(z)
    x=y
    y=z
elif(i==5):
n=int(input('str or int'))
  if(n==1):
    print('palindrome str')
    a=input('enter the value: ')
    print(a[::-1])
  elif(n==2):
      print('palindrome int')
      a=int(input('enter the value: '))
      r=0
      n1=n
while(n1>0):
      a=n1%10
      r=(r*10)+a
      n1=n//10
  else:
      print('select crt option')
else:
    print('click crt option')
          
