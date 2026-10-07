# Program 3 - Guided Practice: Complete the Tuple/Set Code

# Complete: a function that returns a tuple of (min, max) from a list
def get_min_max(numbers):
    return min(numbers), max(numbers)       # blanks -> min(numbers), max(numbers)

low, high = get_min_max([4, 8, 1, 9])       # returned tuple ko unpack kiya
print("Min:", low, "Max:", high)            # Output: Min: 1 Max: 9

# Complete: remove duplicates from this list using a set
marks = [85, 90, 85, 78, 90, 92]
unique_marks = set(marks)                   # blank -> set | duplicates hat jaate hain
print(unique_marks)                         # Output: {90, 92, 85, 78} (order fix nahi)
