# slot 05 - Program 2 — Tax Calculator

monthly_salary = int(input("Enter your monthly salary: "))
annual_salary = monthly_salary * 12
print(annual_salary)

if annual_salary > 1300000:
    print("You are eligible for tax")
else:
    print("You are not eligible for tax")
