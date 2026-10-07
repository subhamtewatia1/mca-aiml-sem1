# slot 04 - Program 5 — Debug: Error 3 (Logic Error)

# BROKEN — runs without crashing, but gives the WRONG answer
math = int(input("Math marks: "))
english = int(input("English marks: "))
science = int(input("Science marks: "))
average = (math + english) / 3    # Wrong! Should include science
print(average)

# FIXED
average = (math + english + science) / 3
print(average)
