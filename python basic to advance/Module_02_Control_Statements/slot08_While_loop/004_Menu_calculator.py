# Program 4 - Independent Task: Menu-Driven Calculator

while True:                                        # menu baar-baar dikhega
    print("1. Add")
    print("2. Subtract")
    print("3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        a = int(input("First number: "))          # input: 5
        b = int(input("Second number: "))         # input: 3
        print("Result:", a + b)                   # Output: Result: 8
    elif choice == "2":
        a = int(input("First number: "))          # input: 10
        b = int(input("Second number: "))         # input: 4
        print("Result:", a - b)                   # Output: Result: 6
    elif choice == "3":
        break                                     # 3 -> program band
    else:
        print("Invalid choice.")                  # 7 jaisa kuch -> Invalid choice.
