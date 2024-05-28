from m1 import *


def AdamNumber(num):
    print('Adam Number')
    check(rev(sqrt(num)),sqrt(rev(num)),'AdamNumber')
def Factorial(num):
    result=fact(num)
    print('Factorial number is: %d=%d'%(num,result))
def ArmstrongNumber(num):
    print('armstrong number')
    check(num,armrev(num),'ArmStrong')
def palindromestr(a):
    print('palindrome str')
    check(a,a[::-1],'Palindrome str')
def palindromeint(a):
    print('palindrome int')
    check(a,rev(a),'Palindrome int')
def evenodd(num):
    evenodd1(num)
