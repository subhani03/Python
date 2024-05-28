num=int(input('enter the value: '))
flag=False
if num==1:
    print(num,"is not a prime no")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
    if flag:
      print(num,"not a prime no")
    else:
      print(num,"prime no")
        


        
        
