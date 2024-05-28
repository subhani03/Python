'''def check(d):
    if(d%2==0):
        return 1
    else:
        return 0

a=int(input('enter the value of a: '))
b=int(input('enter the value of b: '))
c=int(input('enter the value of c: '))
print(check(a))
print(check(b))
print(check(c))
i=check(a)+check(b)+check(c)
if(i==0):
    print(a+b+c)
elif(i==1):
    print(a-b-c)
elif(i==2):
    print(a*b*c)
elif(i==3):
    print(a/b/c)
else:
    print('not valid')'''
'''def check(*num):
    print(sum(num))
check(2,3)
check(2,4,3)
check(2,1,3,4,5)'''
def check(*num):
    a=0
    for x in num:
        a+=x
    return a
print(check(2,3))


    
