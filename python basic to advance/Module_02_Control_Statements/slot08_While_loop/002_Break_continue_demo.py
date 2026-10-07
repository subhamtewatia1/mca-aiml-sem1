# Program 2 - break and continue Demo

for i in range(10):
    if i == 5:
        break                   # 5 aate hi loop khatam
    print(i)                    # Output: 0 1 2 3 4

for i in range(5):
    if i == 2:
        continue                # 2 skip, loop chalta rahega
    print(i)                    # Output: 0 1 3 4
