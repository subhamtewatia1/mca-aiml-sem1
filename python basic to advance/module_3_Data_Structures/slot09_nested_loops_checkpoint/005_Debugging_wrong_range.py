# Program 5 - Debugging Workshop: Broken Program A (Wrong Range)
# Bug: range(1, 3) sirf 1, 2 deta hai -> table 2x2 tak hi banti thi
#
# for i in range(1, 3):
#     for j in range(1, 3):
#         print(i, "*", j, "=", i*j)

# FIXED
for i in range(1, 4):           # Fix: 3 ki jagah 4 -> ab 1, 2, 3
    for j in range(1, 4):       # Fix: yahan bhi 4
        print(i, "*", j, "=", i*j)
# Output: 1*1=1 se 3*3=9 tak, total 9 lines (3x3)
