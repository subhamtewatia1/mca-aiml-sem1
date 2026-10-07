# Program 6 - Debug: Index and Slicing Errors

# Bug 1: Index out of range
marks = [85, 92, 78]
# print(marks[5])               # IndexError: sirf index 0, 1, 2 exist karte hain

# Bug 2: Off-by-one slicing confusion
marks = [85, 92, 78, 88, 95]
print(marks[1:3])               # Output: [92, 78] -> sirf 2 items, kyunki stop (3) include nahi hota

# FIXES
print(marks[2])                 # Bug 1 fixed: valid index | Output: 78
print(marks[1:4])               # Bug 2 fixed: 3 items ke liye stop = 4 | Output: [92, 78, 88]
