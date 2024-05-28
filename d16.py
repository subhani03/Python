

def admin():
    username=input('enter the username: ')
    password=input('enter the password: ')
    if(username =='admin' and password =='admin'):
        print('welcome admin')
def studentregister():
    registernumber=int(input('enter the register number: '))
    studentname=input('enter the studentname: ')
    course=input('enter the your stream: ')
    total=int(input('enter your total: '))
    return studentname,registernumber,course,total
def login():
    name=input('enter the Name: ')
    for x in studentnamelist:
        if (x==name):
            print("logged In")
        
