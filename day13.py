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
        print("It is a ",a," :",x,y)
    else:
        print('It not a',a," : ", x,y)
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact


    
i=int(input('enter the value: '))
if(i!=4):
num=int(input('Enter the Value : '))


if(i==1):
  check(rev(sqrt(num)),sqrt(rev(num)),"Adam Number")
     
elif(i==2):
  print('factorial number: ')
  result=fact(num)
  print('fact no is: %d=%d'%(num,result))

    
elif(i==3):
   check(num,armrev(num),"Armstrong Number")
    
elif(i==4):
    n=int(input('enter the value: 1. str ,2. int :'))
    if(n==1):
     a=input('palindrome str\nenter the value: ')
     check(a,a[::-1],"Palindrome String")
    else:
     a=int(input('palindrome int \n enter the value: '))
     check(a,rev(a),"Palindrome Integer")
else:
    print('choose crt option')
 
    

          
    
    
    

        

    
