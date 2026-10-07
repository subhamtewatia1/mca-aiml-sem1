users = {}

print("===== SECURE EMPLOYEE ACCOUNT SYSTEM =====")

n = int(input("Enter number of accounts to create: "))


for i in range(n):
    print("\n--- Account", i + 1, "---")

    username = input("Enter username: ")

    while username in users:
        print("Username already exists. Please choose another username.")
        username = input("Enter username: ")

    password = input("Enter password: ")

    while True:
        valid = True

        upper = 0
        lower = 0
        number = 0
        special = 0
        space = 0

        for name in password:
            if name.isupper():
                upper += 1

            elif name.islower():
                lower += 1

            elif name.isdigit():
                number += 1

            elif name == " ":
                space += 1

            else:
                special += 1

            valid = True

        if len(password) < 8:
            if valid:
                print("Password rejected!")
            print("Password must contain at least 8 characters.")
            valid = False

        if upper < 1:
            if valid:
                print("Password rejected!")
            print("Password must contain at least one uppercase alphabet.")
            valid = False

        if lower < 1:
            if valid:
                print("Password rejected!")
            print("Password must contain at least one lowercase alphabet.")
            valid = False

        if number < 1:
            if valid:
                print("Password rejected!")
            print("Password must contain at least one digit.")
            valid = False

        if special < 1:
            if valid:
                print("Password rejected!")
            print("Password must contain at least one special character.")
            valid = False

        if space > 0:
            if valid:
                print("Password rejected!")
            print("Password must not contain any space.")
            valid = False

        if valid:
            confirm_password = input("Confirm password: ")

            while confirm_password != password:
                print("Passwords do not match. Please enter the confirm password again.")
                confirm_password = input("Confirm password: ")

            users[username] = password
            print("Account created successfully!")
            break

        password = input("Enter password again: ")

print(users)


print("\n===== EMPLOYEE LOGIN =====")

i = 0

while i < 5:
    username = input("Enter username: ")
    entered = input("Enter password: ")

    if username in users:
        correct_password = users[username]

        if entered == correct_password:
            print("Login successful!")
            print("Welcome", username)
            break

    i += 1
    print("Invalid username or password.")

    if i < 5:
        print("Attempts remaining:", 5 - i)

if i == 5:
    print("Access Denied!")
    print("Maximum login attempts exceeded.")
