# slot 01 - printing with variables

name = "Subham Tewatia"
age = 21
height = 5.8
is_student = True

# way 1 - comma
print("Name:", name, "Age:", age)

# way 2 - plus sign, everything must be a string
print("Name: " + name + " Age: " + str(age))

# way 3 - f string (easiest one)
print(f"my name is {name} and i am {age} years old")
print(f"height {height} ft, student = {is_student}")

# can also do calculation inside f string
print(f"next year i will be {age + 1}")

# way 4 - format()
print("my name is {} and i am {} years old".format(name, age))

# a variable can be changed later
age = 22
print("new age =", age)

# giving values to more than one variable
x, y = 10, 20
print(x, y)

# swapping
x, y = y, x
print("after swap", x, y)
