'''
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input('enter the num: '))
result=fact(num)
print('fact no is: %d=%d'%(num,result))

#adam no using function 
def rev(n):
   r=0 
   while(n<0):
    a=n%10
    r=(r*10)+a
    n=n//a
   return r
def sqrt(n):
    return n*n

def check(a,b):
    if(a==b):
        print("Yes it adam number")
    else:
        print("It is not a adam number ")

n=int(input('enter the no: '))
a=rev(sqrt(n))
b=sqrt(rev(n))
check(a,b)

#armstrong number
def rev(n):
   r=0
   while(n>0):
      a=n%10
      r=r+(a*a*a)
      n=n//10
   return r
num=int(input('enter the number: '))
print(rev(num))

#palindrome
def rev(n):
   r=0
   while(n>0):
       a=n%10
       r=(r*10)+a
       n=n//10
   return r
   print(n)
def check(n1,r):
   if(n1==r):
      print('it is palindrome ')
   else:
      print('it is not palindrome ')
n=int(input('enter the value: '))
n1=n
r=rev(n)
print(n)
print(n1)
print(r)
check(n1,r)
'''
def rev():
   return n[::-1]
def check(x,y):
    if(x==y):
       print('it is a palindrome ')
    else:
       print('it is not palindrome')
n=input('enter the value: ')
x=n
y=rev()
check(x,y)
         

   


      
      



      


