# Program 3 - Guided Practice: Complete the Traversal

# Sum pattern: sum all marks using a traversal loop
marks = [85, 92, 78, 88, 95]
total = 0
for mark in marks:
    total = total + mark            # blank -> total + mark | 85 -> 177 -> 255 -> 343 -> 438
print("Total:", total)              # Output: Total: 438


# Count pattern: count how many marks are >= 90
high_count = 0
for mark in marks:
    if mark >= 90:                  # blank -> mark >= 90  | 92 aur 95
        high_count = high_count + 1
print("High scorers:", high_count)  # Output: High scorers: 2
