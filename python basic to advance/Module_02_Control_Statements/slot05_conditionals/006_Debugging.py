# slot 05 - Program 6 — Debug: Reversed Condition

# WRONG: Condition is reversed
marks = 50
if marks < 35:
    print("Pass")    # This executes! But should say Fail
else:
    print("Fail")

# TASK: Identify the bug and fix it
# FIXED:
if marks >= 35:
    print("Pass")
else:
    print("Fail")
