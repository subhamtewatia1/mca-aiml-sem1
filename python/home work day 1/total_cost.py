# Program 3 - Total cost with discount
# ------------------------------------------------------------
# SIX-STEP FRAMEWORK
#
# Step 1 - Problem samajho:
#   Item ka price aur quantity diya hai. Total cost nikalna hai.
#   Agar total Rs. 500 se zyada ho jaye to flat Rs. 20 discount dena hai.
#
# Step 2 - Input kya hai?
#   price -> float (item ka daam, decimal ho sakta hai)
#   qty   -> int   (kitne item, hamesha pura number)
#
# Step 3 - Output kya hai?
#   total -> final cost (discount lagne ke baad)
#
# Step 4 - Logic (algorithm):
#   1. price aur qty user se lo
#   2. total = price * qty
#   3. agar total > 500 hai, to total = total - 20
#   4. total print karo
#
# Step 5 - Code (neeche)
#
# Step 6 - Test (sample runs):
#   price=100, qty=6 -> 600 > 500 -> 600 - 20 = 580.0
#   price=100, qty=2 -> 200, discount nahi -> 200.0
#   price=250, qty=2 -> 500 exactly, "exceeds" nahi hai -> 500.0
# ------------------------------------------------------------

# Step 2 - inputs lena
price = float(input("Enter the price of the item: "))
qty = int(input("Enter the quantity of the item: "))

# Step 4.2 - total cost nikalna
total = price * qty

# Step 4.3 - discount lagana (sirf 500 se ZYADA par, 500 par nahi)
if total > 500:
    total = total - 20
    print("Discount of Rs. 20 applied!")

# Step 3 - output dikhana
print("Total cost = Rs.", total)
