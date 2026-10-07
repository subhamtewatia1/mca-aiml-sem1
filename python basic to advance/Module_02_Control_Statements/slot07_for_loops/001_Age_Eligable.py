'''age = int(input('Enter a number: '))

if(age < 18):
    print'''

# WAP to accept monthly salary and check the user is eligible for the tax or not
#Tax is applicable if the annual salary is more than 13 lacks
# write a program to accept quantity and price of laptop sold by a sales person where the company gives commission on total based
#where the traffic are:
#if sales is more than 1 lakh , then 10% of commission
# if sales is more 70k but less than 1 lakh ,7%
#if sales is more than 40k but less 70k , 4%
#if sale is less than 40k, 0%

mon_salary = float(input("Enter your monthly salary: "))

ann_salary = mon_salary * 12          # annual = monthly * 12
LIMIT = 1300000                       # 13 lakh ki limit

print("Annual salary = Rs.", ann_salary)

if ann_salary > LIMIT:
    print("Tax is APPLICABLE.")
else:
    print("Tax is NOT applicable.")

# same kaam ek line me, conditional (ternary) operator se:
print("Short form ->", "Tax applicable" if ann_salary > LIMIT else "No tax")

qty = int(input("Enter quantity of laptops sold: "))
price = float(input("Enter price of one laptop: "))

total_sale = qty * price
print("Total sale = Rs.", total_sale)

if total_sale > 100000:
    rate = 10
elif total_sale > 70000:
    rate = 7
elif total_sale > 40000:
    rate = 4
else:
    rate = 0

commission = total_sale * rate / 100
print("Commission rate =", rate, "%")
print("Commission amount = Rs.", commission)
