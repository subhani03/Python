'''
print("hai")
a="hello world"
print("a")

age=13
txt="my name is deeban,and i am {}"
print(txt.format(age))

quantity=3
itemno=4
price=200
myorder="i want {} piece of item {} and the price {}"
print(myorder.format(quantity,itemno,price))

myorder="i want {2} piece of item {0} and the price {1}"
print(myorder.format(quantity,itemno,price))

a="hello,world,name,age"
print(a.split("a"))

print(a.split("e"))

#arithmetic operator

a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)



#assignment operator

a=int(input("enter the value: "))
print(a)
a+=3
print(a)
a-=3
print(a)
a%=3
print(a)

#comparison operator

a=int(input("enter the value: "))
b=int(input("enter the value: "))
print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a>>b)
print(a<<b)

#logical operator
a=int(input('enter the value: '))
print('statement is true?',a>3 and a<5)
print('statement is false?',a>30 or a<6)
print('not statement',not(a>3 and a<5))
'''
#identity operator

a=["rose","lotus"]
b=["rose","lotus"]
c=a
print(a is c)
print(a is not c)
print(a is b)
print(a is not b)
print(a==b)
print(a!=b)
   
      


