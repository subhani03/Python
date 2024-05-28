from d16 import *
studentregisternumber=[401,402,403,404]
studentnamelist=["subani","subashini","simba","gopal"]
courselist=['b.sc','m.sc','b.sc','m.sc']
studentmarktotal=[455,789,456,852]
print(studentregisternumber)
i=int(input('enter the value: '))
if(i==1):
    print('you are in admin page')
    admin()
elif(i==2):
    print('you are in studentregistration page')
    registernumber,studentname,course,total=studentregister()
    studentregisternumber.append(registernumber)
    studentnamelist.append(studentname)
    courselist.append(course)
    studentmarktotal.append(total)
    studentregister()
elif(i==3):
    print('you are in login page')
    login()
