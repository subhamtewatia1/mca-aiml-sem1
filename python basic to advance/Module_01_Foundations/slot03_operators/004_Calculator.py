# slot 03 - simple calculator
# does all the operations on two numbers

x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

add = x + y
sub = x - y
mul = x * y
exp = x ** y
div = x / y
floor = x // y
mod = x % y

print("\nResults:")
print("\tAddition:", add)
print("\tSubtraction:", sub)
print("\tMultiplication:", mul)
print("\tExponent:", exp)
print("\tDivision:", div)
print("\tFloor Division:", floor)
print("\tModulus:", mod)

# note: if y is 0 then division gives ZeroDivisionError


# ================= Sheet program =================
# Program 4 — Independent Task: Simple Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
