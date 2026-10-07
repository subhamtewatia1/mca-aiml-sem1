# Program 6 - Debug: Immutability & Set Order Confusion

# Bug 1: Trying to modify a tuple
point = (10, 20)
# point[0] = 15                 # TypeError: 'tuple' object does not support item assignment

# Bug 2: Assuming a set keeps insertion order (it doesn't!)
numbers = {5, 1, 3, 2, 4}
print(numbers)                  # Output: {1, 2, 3, 4, 5} -> order 5,1,3,2,4 nahi rehta, iss par bharosa mat karo

# FIXES
point = (15, point[1])          # Bug 1 fixed: naya tuple banao
print(point)                    # Output: (15, 20)

numbers = [5, 1, 3, 2, 4]       # Bug 2 fixed: order chahiye to LIST use karo
numbers.sort()
print(numbers)                  # Output: [1, 2, 3, 4, 5]
