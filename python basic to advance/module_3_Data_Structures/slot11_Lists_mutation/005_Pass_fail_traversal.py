# Program 5 - Independent Task: Pass/Fail Traversal Report

marks = [85, 45, 92, 30, 76, 55, 62]
passing = 0
failing = 0

for mark in marks:
    if mark >= 40:                  # 40 ya usse zyada = pass
        passing = passing + 1       # 85, 45, 92, 76, 55, 62
    else:
        failing = failing + 1       # 30

print("Passing:", passing)          # Output: Passing: 6
print("Failing:", failing)          # Output: Failing: 1
