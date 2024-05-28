'''
#lambda func:
def x(a):
    return a+10
x=lambda a:a+10
print(x(5))

def x(a,b):
    return a*b
x=lambda a,b:a*b
print(x(5,6))

def myfunc(n):
    return lambda a:a*n
m=myfunc(2)
print(m(11))
print(m(10))

#mapping:
data=[1,2,3,4,5]
result1=map(lambda x:x*2,data)
print(list(result1))
'''
data=[1,2,3,4,5]
result1=filter(lambda x:x%2==0,data)
print(list(result1))
