# slot 03 - debugging common operator errors
# the broken lines are commented out so the file runs, uncomment one to see the error

# ERROR 1: adding string and number
# age = input('Enter your age: ')
# print(age + 1)            # TypeError: can only concatenate str (not "int") to str
# FIX: convert first
age = "21"
print(int(age) + 1)         # 22

# ERROR 2: joining instead of adding
a = "10"
b = "5"
print(a + b)                # 105, strings are joined
print(int(a) + int(b))      # 15, real addition

# ERROR 3: dividing by zero
# print(10 / 0)             # ZeroDivisionError
y = 0
if y != 0:
    print(10 / y)
else:
    print("cannot divide by zero")

# ERROR 4: converting text that is not a number
# int("hello")              # ValueError
# int("5.5")                # ValueError, use float() first
print(int(float("5.5")))    # 5

# ERROR 5 (logic trap): / vs //
print(7 / 2)                # 3.5
print(7 // 2)               # 3, decimal is cut

# ERROR 6 (logic trap): operator precedence
print(2 + 3 * 4)            # 14, * happens before +
print((2 + 3) * 4)          # 20, brackets first

# ERROR 7 (logic trap): ^ is not power in python
print(2 ^ 3)                # 1, this is XOR
print(2 ** 3)               # 8, this is power


# ================= Sheet program =================
# Program 6 — Debug: Fix the Type Error
# BROKEN — forgot to convert before adding
price = input("Enter price: ")
quantity = input("Enter quantity: ")
# total = price * quantity    # TypeError: can't multiply sequence by non-int of type 'str'

# FIXED
total = int(price) * int(quantity)
print("Total:", total)
