# slot 04 - Program 1 — Guided Decomposition (Write Pseudocode First)

# PROBLEM: Given a price and a discount percentage, calculate the final price.
# Write your UNDERSTAND, BREAK DOWN, and PLAN as comments below
# before writing any code.

# UNDERSTAND:
#   input  -> price of the item, discount percentage
#   output -> final price after discount
#   example: price 1000, discount 10% -> discount 100 -> final price 900
#
# BREAK DOWN:
#   1. take the price from the user
#   2. take the discount percentage from the user
#   3. find the discount amount
#   4. subtract it from the price
#   5. print the final price
#
# PLAN (pseudocode):
#   price    = input as float
#   discount = input as float
#   discount_amount = price * discount / 100
#   final_price     = price - discount_amount
#   print final_price
#

# Now write the CODE:
price = float(input("Enter the price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount amount:", discount_amount)
print("Final price:", final_price)
