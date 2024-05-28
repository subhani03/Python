def input1():
    regno=int(input('enter your regno: '))
    name=input('enter your name: ')
    age=int(input('enter your age: '))
    m1=int(input('enter the value of m1: '))
    m2=int(input('enter the value of m2: '))
    m3=int(input('enter the value of m3: '))
    m4=int(input('enter the value of m4: '))
    m5=int(input('enter the value of m5: '))
    return regno,name,age,m1,m2,m3,m4,m5

def cal(m1,m2,m3,m4,m5):
    if(m1>35 and m2>35 and m3>35 and m4>35 and m5>35):
        tot=m1+m2+m3+m4+m5
        avg=tot/5
        print('you are pass',tot,avg)
        return tot,avg

    else:
        print("you are fail")
        return 0,0
        
    
def selection(avg):
    if(avg==0):
        print("")
    elif(avg>80):
        print("you are selected as a bio maths")
    elif(avg>70):
        print('you are selected as a cs maths')
    else:
        print('select other course')
    

    



