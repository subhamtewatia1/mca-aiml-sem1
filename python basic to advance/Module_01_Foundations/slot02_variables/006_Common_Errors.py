# Program 6 — Debug the Common Errors
# (The broken lines are commented out so the file runs. Uncomment to see each error.)

# ERROR 1: using a variable before defining it
# print(score)                # NameError

# ERROR 2: forgetting quotes
# name = Subham Tewatia            # SyntaxError (Python thinks Subham Tewatia is a variable)

# FIX:
name = "Subham Tewatia"
print(name)

# ERROR 3 (conceptual trap): number stored as string
age = "21"
print(type(age))              # <class 'str'>  -- NOT int, even though it looks like one!
