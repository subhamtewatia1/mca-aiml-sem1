# slot 01 - mini challenge
# make a small report card using input, variables and print

print("---- REPORT CARD ----")

name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter your city: ')

print("\nenter marks out of 100")
python_marks = float(input('Python: '))
maths_marks = float(input('Maths: '))
english_marks = float(input('English: '))

total = python_marks + maths_marks + english_marks
average = total / 3

# grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("\n" + "=" * 32)
print("Name    :", name)
print("Age     :", age)
print("City    :", city)
print("-" * 32)
print("Python  :", python_marks)
print("Maths   :", maths_marks)
print("English :", english_marks)
print("-" * 32)
print("Total   :", total, "/ 300")
print("Average :", round(average, 2), "%")
print("Grade   :", grade)

if average >= 40:
    print("Result  : PASS")
else:
    print("Result  : FAIL")

print("=" * 32)

# to try later:
# ask how many subjects instead of fixing 3
# do not allow marks below 0 or above 100
