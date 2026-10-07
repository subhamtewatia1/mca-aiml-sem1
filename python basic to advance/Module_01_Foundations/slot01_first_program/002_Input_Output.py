# slot 01 - input and output
# input() takes something from the user
# note: input always gives a string
'''
name = input('Enter your name: ')
print("Hello", name)

age_input = input('Enter your age: ')
print(type(age_input))          # str

# print(age_input + 1)          # error, cannot add string and number

age = int(age_input)            # convert to int
print(type(age))
print("next year you will be", age + 1)

# float for decimal values
height = float(input('Enter your height in feet: '))
print("your height is", height)

# adding two numbers
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
print("sum =", x + y)'''

# practice
city = str(input(' which city  you are form?:'))
print("greeting from", city, "!")
age = (input('Enter your age: ')) # Showing this the value error when we gave a string value <type 'int'>
print(city,age)
