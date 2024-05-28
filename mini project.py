
print('1.adam,2.armstrong,3.fact,4.fibonacci,5.palindrome,6.primeno,7.even or odd')
i=int(input('enter the value: '))
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
        n-=1
        print('fact no: ',fact)
elif(i==4):
    print('fibonacci')
    n=int(input('enter the value: '))
    x=1
    y=1
    while(n>=1):
        z=x+y
        n-=1
        print(z)
        x=y
        y=z
elif(i==5):
    print('str,int')
    n=int(input('enter the value: '))
    if(n==1):
        print('palindrome str')
        a=int(input('enter the value: '))
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
elif(i==6):
    n=int(input('enter the value: '))
    flag=False
    if(n==1):
        print("not a prime no")
    elif(n>1):
        for x in range(2,n):
            if(n%x)==0:
                flag=True
                break
        if flag:
              print("not a prime")
        else:
              print("prime no")
elif(i==7):
    n=int(input('enter the value: '))
    if(n%2)==0:
        print('even no')
    else:
        print('odd no')
                  
else:
    print('click crt option')

    

          

    
    
