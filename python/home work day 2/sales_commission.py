# Program 2 - Laptop sales par salesman ka commission nikalna
# ------------------------------------------------------------
# SIX-STEP FRAMEWORK
#
# Step 1 - Problem samajho:
#   Salesman ne kitne laptop beche (quantity) aur ek laptop ka
#   price kya hai - ye do cheez di hain. Total sale nikal ke
#   uspar company commission deti hai.
#
# Step 2 - Input kya hai?
#   qty   -> int   (kitne laptop bike, pura number)
#   price -> float (ek laptop ka daam)
#
# Step 3 - Output kya hai?
#   Total sale, commission rate (%) aur commission amount
#
# Step 4 - Formula / logic:
#   total_sale = qty * price
#   sale > 100000              -> 10%
#   sale > 70000 aur <= 100000 -> 7%
#   sale > 40000 aur <= 70000  -> 4%
#   sale <= 40000              -> 0%
#   commission = total_sale * rate / 100
#
#   NOTE: elif ka order upar se neeche check hota hai, isliye
#   pehla condition jhoot hone par hi doosra check hota hai -
#   "less than" wali baat apne aap handle ho jaati hai.
#
# Step 5 - Code likho (neeche)
#
# Step 6 - Test karo:
#   qty=3 price=50000  -> sale 150000 -> 10% -> 15000
#   qty=1 price=80000  -> sale  80000 ->  7% ->  5600
#   qty=1 price=50000  -> sale  50000 ->  4% ->  2000
#   qty=1 price=30000  -> sale  30000 ->  0% ->     0
# ------------------------------------------------------------

qty = int(input("Enter quantity of laptops sold: "))
price = float(input("Enter price of one laptop: "))

total_sale = qty * price
print("Total sale = Rs.", total_sale)

if total_sale > 100000:               # 1 lakh se zyada
    rate = 10
elif total_sale > 70000:              # 70k se zyada, 1 lakh tak
    rate = 7
elif total_sale > 40000:              # 40k se zyada, 70k tak
    rate = 4
else:                                 # 40k ya usse kam
    rate = 0

commission = total_sale * rate / 100

print("Commission rate =", rate, "%")
print("Commission amount = Rs.", commission)

if rate == 0:
    print("Sorry, is baar koi commission nahi banta.")
