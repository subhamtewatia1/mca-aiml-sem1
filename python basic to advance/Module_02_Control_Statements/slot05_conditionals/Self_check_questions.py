# slot 05 - Self-Check Questions (Post-Lecture)

# Q1. What is the key difference between running three separate if statements and using if/elif/else?
# Ans: Separate ifs  -> Python checks EVERY if, so more than one block can run.
#      if/elif/else  -> Python stops at the FIRST True condition, so only ONE block runs.
marks = 95
# three separate ifs -> prints A, B and C (wrong)
if marks >= 90:
    print("A")
if marks >= 75:
    print("B")
if marks >= 60:
    print("C")
# if/elif/else -> prints only A (correct)
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")

# Q2. If age = 15, which branch executes in: if age >= 18 / elif age >= 13 / else? Trace it.
# Ans: The elif branch.
#      step 1: age >= 18 -> 15 >= 18 -> False, skip
#      step 2: age >= 13 -> 15 >= 13 -> True, run this block and stop
#      step 3: else is skipped
age = 15
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")       # this runs
else:
    print("Child")

# Q3. What does the and operator require to make a combined condition True?
# Ans: BOTH conditions must be True. If even one is False, the result is False.
#      True and True -> True, True and False -> False, False and False -> False
print(True and True, True and False, False and False)

# Q4. Write an if/else pair that prints "Pass" for marks >= 35 and "Fail" otherwise.
# Ans:
marks = 40
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# Q5. Why does the buggy code `if marks < 35: print("Pass")` produce a logic error rather than a crash?
# Ans: The code follows all Python rules (correct syntax, correct types), so Python runs it
#      without any error. Only the MEANING is wrong: the condition is reversed, so a student
#      with less than 35 marks is shown "Pass". Python can't know what we meant, so it can't
#      give an error -> it is a logic error, found only by testing with known values.
