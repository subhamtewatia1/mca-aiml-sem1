# slot 02 - Self-Check Questions (Post-Lecture)

# Q1. What is the difference between a variable and a literal?
# Ans: A literal is the actual fixed value written in code, like 10, 5.8, "Delhi", True.
#      A variable is a name that stores a value, and its value can change later.
#      In  age = 21  -> age is the variable, 21 is the literal.
age = 21
print(age)

# Q2. If x = 10 and then x = "ten", what does type(x) return after each line?
# Ans:
x = 10
print(type(x))      # <class 'int'>
x = "ten"
print(type(x))      # <class 'str'>
#      Python is dynamically typed, so the same variable can hold a different type.

# Q3. Why does age = "22" NOT behave like a number in Python?
# Ans: Because of the quotes, "22" is a string (text), not an int.
#      So maths does not work on it the normal way:
age = "22"
print(type(age))    # <class 'str'>
print(age + "1")    # 221 -> strings are joined, not added
# print(age + 1)    # TypeError: can only concatenate str (not "int") to str
print(int(age) + 1) # 23 -> convert to int first

# Q4. Name the four basic data types introduced in this slot, with one example value for each.
# Ans:
name = "Subham"     # str   -> text
marks = 88          # int   -> whole number
height = 5.8        # float -> decimal number
is_student = True   # bool  -> True / False
print(type(name), type(marks), type(height), type(is_student))

# Q5. What naming convention should Python variables follow, and why avoid camelCase?
# Ans: Python uses snake_case -> all small letters, words joined with underscore
#      e.g. first_name, total_marks, is_student
#      This is the official Python style guide (PEP 8).
#      camelCase (firstName) works, but it is the style of Java/JavaScript, not Python.
#      Mixing styles makes code harder to read, so we follow snake_case everywhere.
#      (CAPITAL_LETTERS are used for constants like PI, and names can't start with a number,
#       contain spaces or -, or be keywords like if, for, class)
