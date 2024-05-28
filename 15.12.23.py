'''
# list
icecream=['vennila','butterscotch','strawberry']
fruits=['orange','mango','apple']
print(fruits)
print(type(fruits))
fruits.append('pomegranate')
print(fruits)
fruits.extend(icecream)
print(fruits)
fruits.insert(3,'pineapple')
print(fruits)
fruits.remove('apple')
print(fruits)
fruits.pop()
print(fruits)
print(fruits.index('orange',0))
print(fruits.count('orange'))
fruits.sort()
print('sorted: ',fruits)
fruits.reverse()
print('reverse list: ',fruits)
icecream1=icecream.copy()
print('copied list',icecream1)

#list stack
stack=[1,2,3,4]
print(stack)
stack.append(5)
print(stack)
stack.pop()
print(stack)

#list queue
from collections import deque
queue=deque(['apple','kiwi','orange'])
print(queue)
queue.append('banana')
print(queue)
queue.popleft()
print(queue)

a=[1,2,3,4,5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

t=123,321
print(t)
print(t[0])
t1=t,(1,2,3,4)
print(t1)
empty=()
singleton='hello'
print(len(empty))
print(len(singleton))
print(singleton)
print(type(singleton))
t=123,321,'tuple'
x,y,z=t
print(t)
print(x)
print(y)
print(z)
'''
basket={'apple','banana','orange'}
print(basket)
print('banana' in basket)
print('mango' not in basket)
a=set('balas')
b=set('balag')
print(a)
print(b)
print(b-a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)







