# Program 5 - Independent Task: Sum Until Sentinel Value

total = 0
num = int(input("Enter a number (0 to stop): "))      # input: 5
while num != 0:                                       # 0 = sentinel, aate hi ruk jao
    total = total + num                               # 5 -> 15 -> 18
    num = int(input("Enter a number (0 to stop): "))  # input: 10, 3, 0
print("Total:", total)                                # Output: Total: 18
