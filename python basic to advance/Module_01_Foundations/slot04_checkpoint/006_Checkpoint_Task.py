# slot 04 - Program 6 — Module 1 Checkpoint Task (Independent)

# Build a small program from scratch using the six-step framework:
# "Given the price and quantity of an item, calculate the total cost
#  and apply a flat Rs. 20 discount if the total exceeds Rs. 500."
# (Conditionals aren't taught until Slot 5 — it's fine to just
#  calculate total and print it; the discount logic returns in Slot 5.)

# STEP 1 - UNDERSTAND:
#   input  -> price of the item, quantity
#   output -> total cost (Rs. 20 less if total is more than 500)
#
# STEP 2 - BREAK DOWN:
#   read price -> read quantity -> multiply -> check > 500 -> print
#
# STEP 3 - PLAN:
#   price = float input, qty = int input
#   cost  = price * qty
#   if cost > 500: cost = cost - 20
#   print cost
#
# STEP 4 - CODE: (below)
#
# STEP 5 - TEST:
#   100, 3 -> 300.0  (no discount)
#   200, 3 -> 580.0  (600 - 20)
#
# STEP 6 - REFLECT:
#   price is float because it can have paise, qty is int (whole items)

price = float(input('Enter a price of the item : '))
qty = int(input('Enter a quantity of the item : '))

cost = price * qty

if cost > 500:
    cost = cost - 20

print("total cost:", cost)
