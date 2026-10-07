# slot 03 - arithmetic operators
# +  -  *  /  //  %  **

x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

print(x + y, x - y, x * y, x / y, x // y, x % y)

# same thing with labels so it is easy to read
print("addition       :", x + y)
print("subtraction    :", x - y)
print("multiplication :", x * y)
print("division       :", x / y)      # always gives decimal
print("floor division :", x // y)     # whole number only
print("remainder      :", x % y)
print("power          :", x ** y)


# ================= Sheet program =================
# Program 2 — Arithmetic Operators Demo
x = 10
y = 3

sum = x + y
print("Sum of two nos:", sum)

diff = x - y
print("Difference of two nos:", diff)

prod = x * y
print("Product of two nos:", prod)

quot = x / y
print("Quotient of two nos:", quot)

modulus = x % y
print("Modulus of two nos:", modulus)

exponent = x ** y
print("Exponent of two nos:", exponent)

fld = x // y
print("Floor division of two nos:", fld)
