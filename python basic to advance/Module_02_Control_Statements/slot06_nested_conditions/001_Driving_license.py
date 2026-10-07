# Program 1 - Nested Condition: Driving Eligibility
# An if inside another if: the inner check only runs when the outer one is True.

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need to get license")
else:
    print("Too young to drive")
