          from m2 import *

choice="y"
while(choice=="y"):
 i=int(input('1.AdamNumber\n2.Factorial\n3.ArmstrongNumber\n4.palindrome\n5.evenodd\nEnter Your Option : '))
 if(i==4):
  pass
 else:
   num=int(input('Enter the value , You want to Check : '))

    
 if(i==1):
    AdamNumber(num)
 elif(i==2):
    Factorial(num)
 elif(i==3):
    ArmstrongNumber(num)
 elif(i==4):
    print('1.str,2.int')
    i=int(input('enter the value: '))                                                                                              
    if(i==1):
        a=input('enter the value: ')
        palindromestr(a)
    elif(i==2):
        a=int(input('enter the value: '))
        palindromeint(a)
    else:
        print('give a crt input')
 elif(i==5):
    evenodd(num)
 else:
    print('choose crt option')

 choice=input("If you want to continue.......(y/n)")
    
    
