'''
for x in range(5):
    print('we are on time %d' %(x))
for x in range(3):
    print(x)
else:
    print('loop end')

lists=[1,2,3]
for x in lists:
 print(x)
 
lists=[[1,2,3],[4,5,6]]
for g in lists:
    for x in g:
        print(x)
        
num=int(input('get the value: '))
factorial=1
if(num>=1):
    for i in range(1,num+1):
        factorial=factorial*i
    print('factorial number is: ',factorial)
        
'''
a="the great"
print(a[:: -1])


a="concept"
print(a[:: -1])
+

a=10
for a in range(10,30,3):
    print(a)

