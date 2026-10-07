# slot 05 - Program 8 — Electricity Bills

name = input("Enter the name of owner: ")
meter = int(input("Enter your meter number: "))
uc = int(input("Enter the units consumed: "))

if uc <= 100:
    bill = uc * 2.5
elif uc >= 101 and uc <= 200:
    bill = (100 * 2.5) + ((uc - 100) * 3.5)
elif uc >= 201 and uc <= 300:
    bill = (100 * 2.5) + ((100) * 3.5) + ((uc - 200) * 4)
elif uc > 300:
    bill = (100 * 2.5) + (100 * 3.5) + (100 * 4) + ((uc - 300) * 4.5)
else:
    print("The total bill not found")

print("The Total bill is:", bill)

# output
# Enter the name of owner: Suman KD
# Enter your meter number: 1001
# Enter the units consumed: 556
# The Total bill is: 2152.0
