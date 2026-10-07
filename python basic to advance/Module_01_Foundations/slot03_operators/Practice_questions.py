# slot 03 - Practice Questions
# (every question asks for input, so running the file asks them one after another)

# 1. WAP to accept radius and display circumference and area of a circle
#    [Circumference = 2πr, Area = πr²]
print("\n--- Q1 Circle ---")
PI = 3.14159
radius = float(input("Enter radius: "))
circumference = 2 * PI * radius
area = PI * radius ** 2
print("Circumference:", round(circumference, 2))
print("Area:", round(area, 2))

# 2. WAP to accept base and height and display area of the triangle
#    [Area = (base × height) / 2]
print("\n--- Q2 Triangle ---")
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = (base * height) / 2
print("Area of triangle:", area)

# 3. WAP to accept Principal, Rate, Time and calculate Simple Interest and Amount
print("\n--- Q3 Simple Interest ---")
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time (years): "))
si = (principal * rate * time) / 100
print("Simple Interest:", si)
print("Amount:", principal + si)

# 4. WAP to accept Quantity and Rate and calculate Total Bill
print("\n--- Q4 Total Bill ---")
qty = int(input("Enter quantity: "))
rate = float(input("Enter rate: "))
print("Total Bill:", qty * rate)

# 5. WAP to accept Bill and calculate GST @ 18%, also calculate CGST and SGST
print("\n--- Q5 GST (CGST + SGST) ---")
bill = float(input("Enter bill amount: "))
gst = bill * 18 / 100
cgst = gst / 2      # 9%
sgst = gst / 2      # 9%
print("GST (18%):", gst)
print("CGST (9%):", cgst)
print("SGST (9%):", sgst)
print("Total with GST:", bill + gst)

# 6. WAP to accept Bill and calculate GST @ 18%, also calculate IGST
print("\n--- Q6 GST (IGST) ---")
bill = float(input("Enter bill amount: "))
igst = bill * 18 / 100     # IGST is the full 18% (used for inter-state sale)
print("IGST (18%):", igst)
print("Total with IGST:", bill + igst)

# 7. WAP to accept Rupees and convert it into Paisa [₹1 = 100p]
print("\n--- Q7 Rupees to Paisa ---")
rupees = float(input("Enter rupees: "))
print(rupees, "rupees =", int(rupees * 100), "paisa")

# 8. WAP to accept Paisa and convert it into Rupees and remaining Paisa [₹1 = 100p]
print("\n--- Q8 Paisa to Rupees ---")
paisa = int(input("Enter paisa: "))
print(paisa, "paisa =", paisa // 100, "rupees and", paisa % 100, "paisa")

# 9. WAP to accept hours and convert it into minutes [1 hour = 60 minutes]
print("\n--- Q9 Hours to Minutes ---")
hours = int(input("Enter hours: "))
print(hours, "hours =", hours * 60, "minutes")

# 10. WAP to accept minutes and convert it into seconds [1 minute = 60 seconds]
print("\n--- Q10 Minutes to Seconds ---")
minutes = int(input("Enter minutes: "))
print(minutes, "minutes =", minutes * 60, "seconds")

# 11. WAP to accept seconds and convert it into minutes and remaining seconds
print("\n--- Q11 Seconds to Minutes ---")
seconds = int(input("Enter seconds: "))
print(seconds, "seconds =", seconds // 60, "minutes and", seconds % 60, "seconds")

# 12. WAP to accept seconds and convert it into hours, minutes and remaining seconds
print("\n--- Q12 Seconds to Hours ---")
seconds = int(input("Enter seconds: "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = seconds % 60
print(seconds, "seconds =", h, "hours", m, "minutes", s, "seconds")

# 13. WAP to accept two different minutes and two different hours and convert it into
#     total hours and total minutes
print("\n--- Q13 Add Time ---")
min1 = int(input("Enter minutes 1: "))
min2 = int(input("Enter minutes 2: "))
hr1 = int(input("Enter hours 1: "))
hr2 = int(input("Enter hours 2: "))
total_minutes = (hr1 + hr2) * 60 + min1 + min2
print("Total minutes:", total_minutes)
print("Total time:", total_minutes // 60, "hours and", total_minutes % 60, "minutes")

# 14. WAP to accept no. of days and convert it into years, months, weeks and days
#     (taking 1 year = 365 days, 1 month = 30 days, 1 week = 7 days)
print("\n--- Q14 Days ---")
days = int(input("Enter number of days: "))
years = days // 365
days_left = days % 365
months = days_left // 30
days_left = days_left % 30
weeks = days_left // 7
days_left = days_left % 7
print(days, "days =", years, "years", months, "months", weeks, "weeks", days_left, "days")

# 15. WAP to accept temperature in Celsius and convert it into Fahrenheit
#     [F = (9/5 × C) + 32]
print("\n--- Q15 Celsius to Fahrenheit ---")
c = float(input("Enter temperature in Celsius: "))
f = (9 / 5 * c) + 32
print(c, "°C =", f, "°F")

# 16. WAP to accept temperature in Fahrenheit and convert it into Celsius
#     [C = 5(F - 32) / 9]
print("\n--- Q16 Fahrenheit to Celsius ---")
f = float(input("Enter temperature in Fahrenheit: "))
c = 5 * (f - 32) / 9
print(f, "°F =", round(c, 2), "°C")

# 17. WAP to accept amount and check how many denominations of ₹2000, ₹500, ₹100 and ₹50
#     are available
print("\n--- Q17 Denominations ---")
amount = int(input("Enter amount: "))
n2000 = amount // 2000
amount = amount % 2000
n500 = amount // 500
amount = amount % 500
n100 = amount // 100
amount = amount % 100
n50 = amount // 50
amount = amount % 50
print("₹2000 notes:", n2000)
print("₹500 notes :", n500)
print("₹100 notes :", n100)
print("₹50 notes  :", n50)
print("Remaining  :", amount)

# 18. WAP to accept Principal, Rate and Time and calculate Compound Interest for the
#     first three years and final amount
print("\n--- Q18 Compound Interest ---")
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = int(input("Enter time (years): "))

amount1 = principal * (1 + rate / 100)
amount2 = amount1 * (1 + rate / 100)
amount3 = amount2 * (1 + rate / 100)
print("Year 1 interest:", round(amount1 - principal, 2), "amount:", round(amount1, 2))
print("Year 2 interest:", round(amount2 - amount1, 2), "amount:", round(amount2, 2))
print("Year 3 interest:", round(amount3 - amount2, 2), "amount:", round(amount3, 2))

final_amount = principal * (1 + rate / 100) ** time
print("Final amount after", time, "years:", round(final_amount, 2))
print("Total compound interest:", round(final_amount - principal, 2))

# 19. WAP to accept weight (in Kilos) and height (in inches) and calculate BMI
#     [BMI = weight / height²], height must be in metres
print("\n--- Q19 BMI ---")
weight = float(input("Enter weight (kg): "))
height_inches = float(input("Enter height (inches): "))
height_m = height_inches * 0.0254       # 1 inch = 0.0254 metre
bmi = weight / height_m ** 2
print("BMI:", round(bmi, 2))

# 20. WAP to accept basic salary and calculate D.A. = 5%, H.R.A. = 8%, T.A. = 6%, P.F. = 10%,
#     GROSS SALARY = Basic + (D.A. + H.R.A. + T.A.) - P.F.
print("\n--- Q20 Salary ---")
basic = float(input("Enter basic salary: "))
da = basic * 5 / 100
hra = basic * 8 / 100
ta = basic * 6 / 100
pf = basic * 10 / 100
gross = basic + (da + hra + ta) - pf
print("Basic :", basic)
print("D.A.  :", da)
print("H.R.A.:", hra)
print("T.A.  :", ta)
print("P.F.  :", pf)
print("Gross Salary:", gross)

# 21. WAP to accept a number and display its square.
print("\n--- Q21 Square ---")
num = int(input("Enter a number: "))
print("Square:", num ** 2)

# 22. WAP to accept a number and display its cube.
print("\n--- Q22 Cube ---")
num = int(input("Enter a number: "))
print("Cube:", num ** 3)

# 23. WAP to accept two numbers and solve the following equation a² + b²
print("\n--- Q23 a² + b² ---")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("a² + b² =", a ** 2 + b ** 2)
