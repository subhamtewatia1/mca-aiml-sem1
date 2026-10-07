# slot 04 - Program 4 — Debug: Error 2 (Type Error)

# BROKEN
# math = input("Math marks: ")
# total = math + 5    # Can't add string + int -> TypeError

# FIXED
math = int(input("Math marks: "))
total = math + 5
print("Total:", total)
