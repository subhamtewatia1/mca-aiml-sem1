# slot 02 - variable types
# str = text, int = whole number, float = decimal, bool = True/False

name = "Subham Tewatia"
age = 21
height = 5.8
is_student = True

# type() tells the data type
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print(type(name), type(age), type(height), type(is_student))

# python decides the type by itself
value = 10
print(value, type(value))
value = "ten"
print(value, type(value))       # same name, now it is a string

# ---- type casting ----
a = int("25")       # string to int
b = float("3.5")    # string to float
c = str(21)         # int to string
d = int(5.9)        # float to int -> 5, decimal is cut not rounded
e = float(7)        # 7.0

print(a, b, c, d, e)
print(round(5.9))   # round() gives 6

# bool -> 0, 0.0 and "" are False, everything else is True
print(bool(0), bool("hi"))

# why casting is needed with input
s1 = "10"
s2 = "5"
print(s1 + s2)              # 105, joins the strings
print(int(s1) + int(s2))    # 15, real addition

# int("hello")  -> ValueError, this cannot be converted


# ================= Sheet program =================
# Program 2 — Inspecting Types with type()

name = "Subham Tewatia"
age = 21
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
