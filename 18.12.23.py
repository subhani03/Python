'''
dic={'name':'siddha','age':23}
print(dic)
dic['guide']=987
print(dic)
del dic['age']
print(dic)
print(list(dic))
print(sorted(dic))
print('guido' in dic)
a=dict([('bala',384),('rakesh',456)])
print(a)
dist={x:x**2 for x in (2,4,6)}
print(dist)
a=dict(a=98,b=98,c=90)
print(a)
dic['guido']=897
print(dic)
print('guido' in dic)

x=10
if (x==10)
print(x)

print(x)

x=100
y=5
z=y+x
print(z)

x=['anna','annamalai']
print(x[2])

x='Nandhini'
x.reverse()

def fact(n):
    r=1
    for i in range(1,n):
        r=r*i
    return r
print(fact(5))

try:
    x=int(input('enter a value: '))
    y=10/x
    print('result: ',y)
except ValueError:
    print('valid a input')
except ZeroDivisionError:
    print('anything cannot divide by zero')

try:
    x=int(input('enter a value: '))
    z=x+y
    print('addition value: ',y)
except valueError:
    print('crt value')

    
def rev(n):
    r=0
    while(n>0):
        a=n%10
        r=r+(a*a*a)
        n=n//10
        return n
print(rev(n))

a='hello'
b=100
c=a+b
print(c)
'''





