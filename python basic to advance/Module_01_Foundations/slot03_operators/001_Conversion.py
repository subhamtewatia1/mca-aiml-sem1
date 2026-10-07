# slot 03 - type conversion
# input always gives a string, so convert it before doing maths

age_input = input('Enter your age: ')
print(type(age_input))
# print(age_input + 1)  if we add string with number it gives a type error

age = int(age_input)
print(type(age))

print(age + 1)

# some more conversions
marks = float(input('Enter your marks: '))
print(marks, type(marks))

print(int(5.9))     # 5, decimal part is removed
print(str(21) + " years")
print(bool(0), bool(1))


# ================= Sheet program =================
# Program 1 — String Input vs. Converted Number
age_input = input("Enter your age: ")
print(type(age_input))

# TYPEERROR : print(age_input + 1)

age = int(age_input)
print(type(age))

print(age + 1)    # works now that it's an int
