# Program 3 - Guided Practice: Scholarship Eligibility
# Complete this multi-criteria check
age = int(input("Enter age: "))
gpa = float(input("Enter GPA: "))
income = int(input("Enter family income: "))

eligible = (age >= 18) and (gpa >= 3.0) and (income < 500000)
if eligible:
    print("Eligible for scholarship")
else:
    print("Not eligible")

# Same rule written with the nested (one condition per level) version
if age >= 18:
    if gpa >= 3.0:
        if income < 500000:
            print("Eligible for scholarship")
        else:
            print("Not eligible: family income too high")
    else:
        print("Not eligible: GPA below 3.0")
else:
    print("Not eligible: under 18")
