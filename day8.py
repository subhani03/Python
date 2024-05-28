
a="madam"
b=a[::-1]
if(a==b):
    print("palindrome")
else:
    print("not a palindrome")
#factorial using while loop

i=int(input('enter the number: '))
fact=1
while(i>0):
     fact=fact*i
     i-=1
print('fact no: ',fact)
  
i=int(input('enter the value: '))
x=1
y=1
while(i>=1):
    z=x+y
    i-=1
    print(z)
    x=y
    y=z

   
#adam number
n=int(input('enter the value: '))
n1=n*n
print("square of given value:",n1)
r=0
while(n>0):
    a=n%10
    r=(r*10)+a
    n=n//10
print('reverse of given value: ',r)
b=r*r
print('square of reverse value: ',b)
c=0
while(b>0):
    a=b%10
    c=(c*10)+a
    b=b//10
print('reverse of square value: ',c)   
print(c,b)
if(n1==c):
    print('adam no')
else:
    print('not a adam no')


n=int(input('enter the number '))
n1=n*n
r=0
while(n>0):
    a=n%10
    r=(r*10)+a
    n=n//10
    b=r*r
    
c=0
while(b>0):
    a=b%10
    c=(c*10)+a
    b=b//10
if(n1==c):
    print('adam no')
else:
    print('not a adam no')
    
#armstrong number
n=int(input('enter the number: '))
r=0
while(n>0):
    a=n%10
    r=r+(a*a*a)
    n=n//10
    print(r)

    
     
