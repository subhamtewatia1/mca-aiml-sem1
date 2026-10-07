# Program 6 - Debug: Wrong Nesting Level
# WRONG: 'Need to get license' also prints for users under 18
# because it's nested at the wrong level
age = 15
has_license = False

if age >= 18:
    print("Old enough")
if has_license:
    print("Can drive")
else:
    print("Need to get license")   # BUG: prints even though age < 18

# FIXED: put the has_license check INSIDE the age check
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need to get license")
else:
    print("Too young to drive")
