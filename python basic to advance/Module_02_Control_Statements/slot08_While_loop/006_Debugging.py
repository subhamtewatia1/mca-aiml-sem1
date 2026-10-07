# Program 6 - Debug: Infinite Loop
# Bug: i = i + 1 missing tha, isliye i hamesha 0 -> 0 forever print hota

i = 0
while i < 10:
    print(i)                    # Output: 0 1 2 3 4 5 6 7 8 9
    i = i + 1                   # Fix: yahi line missing thi
