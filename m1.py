def rev(n):
    r=0
    while(n>0):
        a=n%10
        r=(r*10)+a
        n=n//10
    return r
def sqrt(n):
    return n*n
def armrev(n):
    r=0
    while(n>0):
        a=n%10
        r=r+(a*a*a)
    return r
def check(x,y,a):
    if(x==y):
        print('it is true',a,' : ',x,y)
    else:
        print('it is not true',a,' : ',x,y)
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
def evenodd1(num):
    if(num%2==0):
        print('it is even')
    else:
        print('it is odd')
