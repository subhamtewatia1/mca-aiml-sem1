# slot 05 - Program 4 — Independent Task: Movie Ticket Pricing

# Build a ticket price checker:
# Age < 5: Free
# Age 5-17: Rs. 150
# Age 18-59: Rs. 300
# Age 60+: Rs. 100 (senior discount)
age = int(input("Enter age: "))

# write the if/elif/else chain here
if age < 5:
    print("Ticket: Free")
elif age <= 17:
    print("Ticket: Rs. 150")
elif age <= 59:
    print("Ticket: Rs. 300")
else:
    print("Ticket: Rs. 100 (senior discount)")
