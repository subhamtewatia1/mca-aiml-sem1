# slot 05 - Program 3 — Guided Practice: Grade Assigner

# Complete this grade assigner
marks = int(input("Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:    # Complete this condition
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"      # Complete this line

print("Grade:", grade)

# Test: marks=95 -> A, marks=75 -> B, marks=50 -> C
# (note: 50 is below 60, so with this code it actually gives F)
