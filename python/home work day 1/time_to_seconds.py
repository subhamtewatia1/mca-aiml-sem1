# Program 1 - hours, minutes, seconds ko total seconds me convert karna

hrs = int(input("Enter hours: "))
mins = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))

total = hrs * 3600 + mins * 60 + sec

print("Total seconds =", total)
