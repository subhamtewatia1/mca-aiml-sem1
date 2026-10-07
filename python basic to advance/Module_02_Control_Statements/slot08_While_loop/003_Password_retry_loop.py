# Program 3 - Guided Practice: Password Retry Loop

correct_password = "python123"
entered = ""
while entered != correct_password:                 # blank 1 -> correct_password
    entered = input("Enter password: ")            # input: abc, phir python123
    if entered != correct_password:
        print("Wrong password. Try again.")        # blank 2 -> abc par ye print hoga
print("Access granted")                            # python123 par -> Access granted
