# slot 02 - working with variables

name = "Subham Tewatia"
Age = 21
height = 5.8
is_student = True
is_teacher = False

# ---- text ----
print(name.upper())
print(name.lower())
print(name.title())
print(len(name), "characters")
print(name.replace("Subham", "Shubham"))
print(name.split())             # ['Subham', 'Tewatia']

first, last = name.split()
print("first name:", first, "last name:", last)
print("initials:", first[0] + last[0])

# ---- numbers ----
print("age next year:", Age + 1)
print("age in months:", Age * 12)
print("height in cm :", height * 30.48)
print(Age / 2)      # normal division, gives decimal
print(Age // 2)     # floor division, whole number only
print(Age % 2)      # remainder, 1 means odd
print(Age ** 2)     # power

# ---- true / false ----
print("adult?", Age >= 18)
print(is_student and Age >= 18)
print(is_student or is_teacher)
print(not is_teacher)

# ---- short forms ----
score = 100
score += 50
print(score)
score -= 30
print(score)
score *= 2
print(score)
score /= 4
print(score)

# ---- final summary ----
print("=" * 32)
print("Name    :", name)
print("Age     :", Age, "years")
print("Height  :", height, "ft =", round(height * 30.48, 1), "cm")
print("Student :", is_student)
print("Teacher :", is_teacher)
print("=" * 32)


# ================= Sheet program =================
# Program 4 — Independent Task: 5-Variable Profile

# Create 5 variables and print each with its type
my_name = input("enter your name")
my_age = int(input("enter your age"))
my_city = input("enter your city")
my_height = float(input("enter your height"))
is_employed = bool(input("enter your employment status"))  # False

print(my_name, my_age, my_city, my_height, is_employed)
print(type(my_name), type(my_age), type(my_city), type(my_height), type(is_employed))
