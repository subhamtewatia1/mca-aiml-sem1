# slot 02 - practice questions

# q1 store name age city and print
name = "Subham Tewatia"
age = 21
city = "Delhi"
print(f"{name} is {age} years old and lives in {city}")

# q2 swap two numbers without third variable
a = 5
b = 10
print("before:", a, b)
a, b = b, a
print("after:", a, b)

# q3 area and perimeter of rectangle
length = 12.5
width = 8
area = length * width
perimeter = 2 * (length + width)
print("area =", area, "perimeter =", perimeter)

# q4 celsius to fahrenheit
celsius = 37
fahrenheit = (celsius * 9 / 5) + 32
print(celsius, "C =", fahrenheit, "F")

# q5 seconds into hours minutes seconds
total_seconds = 5000
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(total_seconds, "sec =", hours, "h", minutes, "m", seconds, "s")

# q6 total and average of 3 marks
python_marks = 88
maths_marks = 76
english_marks = 91
total = python_marks + maths_marks + english_marks
average = total / 3
print("total =", total, "average =", round(average, 2))

# q7 simple interest
principal = 15000
rate = 7.5
time = 3
interest = (principal * rate * time) / 100
print("interest =", interest, "amount =", principal + interest)

# q8 swap first and last letter of a word
word = "python"
swapped = word[-1] + word[1:-1] + word[0]
print(word, "->", swapped)

# to try later:
# area of a circle, sum and product of two numbers, price after discount


# ================= Sheet program =================
# Program 3 — Guided Practice: Fill in the Blanks

# Complete these variable assignments
name = "Subham tewatia"       # your name (string)
birth_year = 2005       # your birth year (integer)
gpa = 9.2               # a GPA value (float)
is_indian = True        # True or False (boolean)

print(name, birth_year, gpa, is_indian)
print(type(name), type(birth_year))
