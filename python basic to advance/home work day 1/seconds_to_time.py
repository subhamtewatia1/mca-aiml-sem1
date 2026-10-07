# Program 2 - total seconds ko hours, minutes aur seconds me convert karna

total = int(input("Enter total seconds: "))

hrs = total // 3600
mins = (total % 3600) // 60
sec = total % 60

print("Hours =", hrs)
print("Minutes =", mins)
print("Seconds =", sec)
