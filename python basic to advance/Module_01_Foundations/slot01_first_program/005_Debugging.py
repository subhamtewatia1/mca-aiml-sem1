# slot 01 - debugging
# 3 types of errors -> syntax, runtime, logical

# 1) SYNTAX ERROR - python cannot even run the file
# print("hello"          <- bracket not closed
# print "hello"          <- old python 2 style
# if 5 > 3               <- colon missing
'''
if 5 > 3:
    print("5 is bigger than 3")

# 2) RUNTIME ERROR - file runs then stops in the middle
# print(marks)           <- NameError, variable not made yet
# print("age: " + 21)    <- TypeError, string + int
# int("hello")           <- ValueError
# print(10 / 0)          <- ZeroDivisionError
# marks = [90, 85, 77]
# print(marks[5])        <- IndexError, only 0 1 2 are there

# try / except stops the program from crashing
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

# 3) LOGICAL ERROR - no error message but wrong answer
marks = [80, 90, 70]

avg = sum(marks) / 2        # wrong, divided by 2 instead of 3
print("wrong average =", avg)

avg = sum(marks) / len(marks)   # correct
print("right average =", avg)

# how i find my mistake -> put print() in between and check the values
total = 0
for m in marks:
    total = total + m
    print("added", m, "total is now", total)

print("final total =", total)'''

