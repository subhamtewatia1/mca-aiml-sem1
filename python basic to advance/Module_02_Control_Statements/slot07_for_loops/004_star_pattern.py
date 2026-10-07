#WAP to print a right angle triangle of stars for the given number of rows
rows = int(input("How many rows? "))

for i in range(1, rows + 1):
    print("*" * i)

print()

#WAP to print an inverted triangle of stars
for i in range(rows, 0, -1):
    print("*" * i)

print()

#WAP to print a pyramid of stars
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

print()

#WAP to print the same right angle triangle using a nested loop
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
