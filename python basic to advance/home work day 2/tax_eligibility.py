# Program 1 - Monthly salary lo aur batao tax lagega ya nahi
# ------------------------------------------------------------
# SIX-STEP FRAMEWORK
#
# Step 1 - Problem samajho:
#   User ki MONTHLY salary di hai. Tax tabhi lagta hai jab
#   ANNUAL (saal bhar ki) salary 13 lakh se zyada ho.
#
# Step 2 - Input kya hai?
#   mon_salary -> float (monthly salary, decimal ho sakti hai)
#
# Step 3 - Output kya hai?
#   Annual salary + "Tax applicable" ya "Tax not applicable"
#
# Step 4 - Formula / logic:
#   annual = monthly * 12
#   agar annual > 1300000  -> tax lagega
#   warna                  -> tax nahi lagega
#
# Step 5 - Code likho (neeche)
#
# Step 6 - Test karo:
#   110000 -> annual 1320000 -> Tax APPLICABLE
#   100000 -> annual 1200000 -> Tax NOT applicable
# ------------------------------------------------------------

'''mon_salary = float(input("Enter your monthly salary: "))

ann_salary = mon_salary * 12          # annual = monthly * 12
LIMIT = 1300000                       # 13 lakh ki limit

print("Annual salary = Rs.", ann_salary)

if ann_salary > LIMIT:
    print("Tax is APPLICABLE.")
else:
    print("Tax is NOT applicable.")

# same kaam ek line me, conditional (ternary) operator se:
print("Short form ->", "Tax applicable" if ann_salary > LIMIT else "No tax")'''

'''qty = int(input("Enter quantity of laptops sold: "))
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
    print("Sorry, is baar koi commission nahi banta.")'''

