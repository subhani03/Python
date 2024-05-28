#input and output
#arithmetic operator
'''
a=int(input("enter the value: "))
b=int(input("enter the value: "))
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a//b)
print(a**b)

#assignment operator
a=int(input("enter the value: "))
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a%=3
print(a)
a//=3
print(a)
a**=3
print(a)

#day4 workout
#simple if
name=input('enter a name: ')
age=int(input('enter a age: '))
if(age>20):
 print(name+" you are eligible to govt examination")
else:
 print("not eligible to write the exam")
 
#elif

m1=99
m2=89
m3=100
if(m1>m2):
    print("very good performmance")
elif(m2>m3):
     print("good performmance")
elif(m3>m1):
      print("first class")
else:
    print("second class")

#nested if

m1=99
m2=89
m3=100
if(m1>m2 ):
    print("very good performance")
    if(m1>m3):
        print("good performance")
    else:
        print("bad performance")
else:
    print("first class")
    '''
age=int(input('enter the value: '))
place=input('enter the value: ')
if(age>20):
    print("you are eligible to vote")
    if(place=="myd"):
        print("you are eligible to vote")
    else:
        print("you are non eligible")
else:
    print("you are not eligible to vote")

     

            
