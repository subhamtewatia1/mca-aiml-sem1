# slot 04 - Program 2 — Full Framework Walkthrough: Marks Average
# Follow all six steps as comments, then code (see Section 2 worked example)

# STEP 1 - UNDERSTAND:
#   input  -> marks of maths, english, science
#   output -> total and average of the three marks
#
# STEP 2 - BREAK DOWN:
#   read 3 marks -> add them -> divide by 3 -> print
#
# STEP 3 - PLAN:
#   math, english, science = int inputs
#   total   = math + english + science
#   average = total / 3
#   print total and average
#
# STEP 4 - CODE: (below)
#
# STEP 5 - TEST:
#   80, 90, 70 -> Total: 240, Average: 80.0
#
# STEP 6 - REFLECT:
#   int() is needed because input() gives a string
#   / gives a decimal average, // would cut the decimal

math = int(input("Math marks: "))
english = int(input("English marks: "))
science = int(input("Science marks: "))

total = math + english + science
average = total / 3

print("Total:", total)
print("Average:", average)
