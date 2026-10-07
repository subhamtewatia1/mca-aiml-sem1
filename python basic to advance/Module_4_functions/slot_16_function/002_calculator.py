# Q1 - wap to design a non parametrised func tion that accept two number from the user and accept two nos from the user and add them
#Q-1 Wap to call the non-parametrised function named addition()

def addition():
     num1 = int(input("Enter first number: ")) # num basically is a local variable of the given function
     num2 = int(input("Enter second number: "))
     sum = num1 + num2
     print(f"The sum is {sum}")
     addition()
#Q-2 wap a to design a parametrised
#Q3 wap a program circle  that accepts radius as an arguments and calculator the circumstances and returns the value and does not

def multiplication():
    num1 = int(input("Enter first number: "))
def subtraction(no1,no2):
   ''' if no1 > no2:
          diff = no1 - no2
    else:
         diff = no2 - no1'''

print(f"The difference  is {diff}")

addition()
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
subtraction(number1,number2)


def circle (radius):
     circumference = 2 * math.pi * radius
     return circumference

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
x=subtraction(num1,num2)
print(x)
print(type(x))


import math
def subtraction(no1,no2):
     diff = math.fabs(no1-no2)
print(f"The difference  is {diff}")