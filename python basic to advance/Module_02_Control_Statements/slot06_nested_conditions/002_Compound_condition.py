# Program 2 - Same Logic, Compound Condition
# Same result as Program 1, but with 'and' instead of nesting.
# Note: we lose the separate "Need to get license" message,
# because both failures now fall into the same else.

age = 20
has_license = True

if age >= 18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")
