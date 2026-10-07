# slot 02 - declaring variables
# a variable is just a name that keeps a value
# name = value

name = "Subham Tewatia"
Age = 21
height = 5.8
is_student = True
is_teacher = False

print(name, Age, height, is_student, is_teacher)

# printing with labels looks better
print("Name    :", name)
print("Age     :", Age)
print("Height  :", height)
print("Student :", is_student)
print("Teacher :", is_teacher)

# rules for names
# ok    -> name, age2, first_name, _total
# not ok-> 2age (starts with number), first-name (minus sign), my name (space)
# class, for, if etc are keywords, cannot be used
# name and Name are two different variables

first_name = "Subham"
last_name = "Tewatia"
print(first_name, last_name)

# value can be changed anytime
Age = 22
print("new age =", Age)

# more than one variable in one line
x, y, z = 10, 20, 30
print(x, y, z)

p = q = r = 100
print(p, q, r)

# capital letters are used when the value should not change
PI = 3.14159
MAX_MARKS = 100
print(PI, MAX_MARKS)


# ================= Sheet program =================
# Program 1 — Declaring Variables of Each Type

name = "Subham Tewatia"
age = 21
height = 5.8
is_student = True
print(name, age, height, is_student)
