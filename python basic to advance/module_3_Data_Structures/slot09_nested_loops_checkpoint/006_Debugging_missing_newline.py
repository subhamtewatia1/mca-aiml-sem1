# Program 6 - Debugging Workshop: Broken Program B (Missing Newline)
# Bug: inner loop ke baad print() nahi tha, isliye sab ek hi line me
#      aata tha -> *************** (15 stars ek line me)
#
# for row in range(3):
#     for col in range(5):
#         print("*", end="")

# FIXED
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()                     # Fix: har row ke baad nayi line
# Output:
# *****
# *****
# *****
