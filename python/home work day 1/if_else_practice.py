# ============================================================
# Day 2 - if / elif / else , logical operator , conditional operator
# ============================================================


# ------------------------------------------------------------
# Q1. Age check (if - else ka basic use)
# ------------------------------------------------------------
age = int(input('Enter your age: '))

if age < 18:
    print("You are NOT eligible to vote.")
else:
    print("You are eligible to vote.")

# same kaam CONDITIONAL (ternary) OPERATOR se, ek hi line me:
print("Short form ->", "Eligible" if age >= 18 else "Not eligible")

print()  # khali line, output saaf dikhe


# ------------------------------------------------------------
# Q2. WAP to accept monthly salary and check if the user is
#     eligible for tax or not.
#     Tax applicable if the ANNUAL salary is more than 13 lakhs.
# ------------------------------------------------------------
# NOTE: Python me 'Float' nahi chalta, chhota 'float' hota hai
mon_salary = float(input('Enter your monthly salary: '))

ann_salary = mon_salary * 12          # annual = monthly * 12
print("Annual salary = Rs.", ann_salary)

if ann_salary > 1300000:              # 13 lakhs
    print("Tax is APPLICABLE.")
else:
    print("Tax is NOT applicable.")

print()


# ------------------------------------------------------------
# Q3. Accept quantity and price of laptops sold by a salesperson.
#     Company gives commission on total sales:
#       sales more than 1 lakh              -> 10%
#       more than 70k but less than 1 lakh  ->  7%
#       more than 40k but less than 70k     ->  4%
#       less than 40k                       ->  0%
# ------------------------------------------------------------
qty = int(input('Enter quantity of laptops sold: '))
price = float(input('Enter price of one laptop: '))

sales = qty * price
print("Total sales = Rs.", sales)

# ELIF LADDER - upar se neeche check hota hai aur pehli sahi
# condition par ruk jata hai, isliye range apne aap ban jati hai
if sales > 100000:
    rate = 10
elif sales > 70000:                   # yaha tak aaya matlab sales <= 100000
    rate = 7
elif sales > 40000:                   # yaha tak aaya matlab sales <= 70000
    rate = 4
else:
    rate = 0

commission = sales * rate / 100

print("Commission rate =", rate, "%")
print("Commission = Rs.", commission)

# LOGICAL OPERATOR (and) se bhi likh sakte hain, elif ke bina.
# Tab har range dono taraf se khud likhni padegi:
#
# if sales > 100000:
#     rate = 10
# if sales > 70000 and sales <= 100000:
#     rate = 7
# if sales > 40000 and sales <= 70000:
#     rate = 4
# if sales <= 40000:
#     rate = 0
