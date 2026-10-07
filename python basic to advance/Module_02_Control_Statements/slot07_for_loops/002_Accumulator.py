# write a program to accept the number the user and calculate total from one to the given number
num = int(input("what is your number? "))
total = 0
for i in range(1, num + 1):
    total = total + i
print("the total is:", total)

#WAP a program to accept a number to calculate the factorial
num = int(input("what is your number? "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("the factorial is:", fact)
