# Program 1 - Input Validation Loop (Age)

age = -1                                          # invalid value se shuru, taaki loop chale
while age < 0 or age > 120:                       # jab tak age galat hai, poochte raho
    age = int(input("Enter your age (0-120): "))  # input: -5 / 150 / 25
    if age < 0 or age > 120:
        print("Invalid. Try again.")              # -5 ya 150 par -> Invalid. Try again.
print("Valid age recorded:", age)                 # 25 par -> Valid age recorded: 25
