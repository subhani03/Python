regno=int(input('enter the reg no: '))
name=input('enter your name: ')
age=int(input('enter your age: '))
m1=int(input('enter the value: '))
m2=int(input('enter the value: '))
m3=int(input('enter the value: '))
m4=int(input('enter the value: '))
m5=int(input('enter the value: '))
if(m1>35 and m2>35 and m3>35 and m4>35 and m5>35):
    print('pass')
    total=m1+m2+m3+m4+m5
    print('total: ',m1+m2+m3+m4+m5)
    percentage=total/5
    print('percentage: ',total/5)
    if(percentage>80):
        print('bio maths')
    elif(percentage>70):
        print('cs maths ')
    else:
        print('select other course ')
else:
    print('fail')
          
    




