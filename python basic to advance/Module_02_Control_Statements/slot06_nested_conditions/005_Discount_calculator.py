# Program 5 - Independent Task: Multi-Tier Discount Calculator
# A store gives discounts based on TWO factors: membership AND purchase amount
# Member + purchase >= 1000: 20% off
# Member + purchase < 1000: 10% off
# Non-member + purchase >= 1000: 5% off
# Non-member + purchase < 1000: no discount
is_member = input("Are you a member? (yes/no): ") == "yes"
amount = int(input("Enter purchase amount: "))

# Nested if/else logic
if is_member:
    if amount >= 1000:
        discount = 20
    else:
        discount = 10
else:
    if amount >= 1000:
        discount = 5
    else:
        discount = 0

final_amount = amount - (amount * discount / 100)
print("Discount:", discount, "%")
print("Final amount:", final_amount)
