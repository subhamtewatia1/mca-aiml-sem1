#WAP to accept the name from the user and print it 7 times
name = input("what is your name? ")
for i in range(1, 8):
    print(i, "Hello " + name + "!")

#when we try to run number in the reversse
for i in range(200, 45, -3):
    print(i, "Hello " + name + "!")

# write a program to accept the number the user and calculate total from one to the given number
num = int(input("what is your number? "))
total = 0
for i in range(1, num + 1):
    total = total + i
print("the total is:", total)

#WAP to check a letter is present in the name or not using in / not in
letter = input("Which letter to search? ")
if letter in name:
    print(letter, "is present in the name")
else:
    print(letter, "is not present in the name")

if letter not in name:
    print("not in ->", letter, "missing from", name)
#write the name using the input use
for ch in name:
    print(ch)

# same name ek hi line me -> end="" se newline hat jata hai
for ch in name:
    print(ch, end="")
print()

