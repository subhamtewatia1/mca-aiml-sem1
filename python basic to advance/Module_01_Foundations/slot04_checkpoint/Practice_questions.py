# slot 04 - Practice Questions
# (every question asks for input, so running the file asks them one after another)

PI = 3.14159

# 1. WAP to accept the required variables and print the output of: ⅓b²h
print("\n--- Q1 ⅓b²h ---")
b = float(input("Enter b: "))
h = float(input("Enter h: "))
result = (1 / 3) * b ** 2 * h
print("⅓b²h =", round(result, 2))

# 2. WAP to accept the required variables and print the output of: πr²h
print("\n--- Q2 πr²h ---")
r = float(input("Enter r: "))
h = float(input("Enter h: "))
result = PI * r ** 2 * h
print("πr²h =", round(result, 2))

# 3. WAP to accept the required variables and print the output of: √((x2 − x1)² + (y2 − y1)²)
print("\n--- Q3 Distance ---")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5     # ** 0.5 means square root
print("Distance =", round(distance, 2))

# 4. WAP to accept the required variables and print the output of: (-b + √(b² − 4ac)) / 2a
print("\n--- Q4 Quadratic root ---")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
root = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)     # brackets around 2a are needed
print("Root =", root)
# note: if b² − 4ac is negative, the answer will be a complex number

# 5. WAP to accept the required variables and print the output of: a^(m−n)
print("\n--- Q5 a^(m-n) ---")
a = float(input("Enter a: "))
m = int(input("Enter m: "))
n = int(input("Enter n: "))
print("a^(m-n) =", a ** (m - n))

# 6. WAP to accept the day and month and then calculate which day is it of the year.
#    Assuming all months have 30 days.  Eg: Day = 5, Month = 2, Output = 35 Days
print("\n--- Q6 Day of the year ---")
day = int(input("Enter day: "))
month = int(input("Enter month: "))
day_of_year = (month - 1) * 30 + day
print("Output =", day_of_year, "Days")

# 7. WAP to accept two numbers and swap them using third variable.
print("\n--- Q7 Swap with third variable ---")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Before swap: x =", x, "y =", y)
temp = x
x = y
y = temp
print("After swap : x =", x, "y =", y)

# 8. WAP to accept two numbers and swap them without using third variable.
print("\n--- Q8 Swap without third variable ---")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Before swap: x =", x, "y =", y)
x = x + y
y = x - y
x = x - y
print("After swap : x =", x, "y =", y)
# python short way: x, y = y, x

# 9. WAP to accept either 1 or 0 and print the alternate.
#    Eg: Input = 1, Output = 0 / Input = 0, Output = 1
print("\n--- Q9 Alternate of 1 or 0 ---")
num = int(input("Enter 1 or 0: "))
print("Output =", 1 - num)

# 10. Movie Ticket Booking
#     A cinema charges a fixed price of ₹250 per ticket.
#     WAP to accept the number of tickets and calculate and display the total ticket amount.
print("\n--- Q10 Movie Ticket Booking ---")
TICKET_PRICE = 250
tickets = int(input("Enter number of tickets: "))
print("Total ticket amount: ₹", tickets * TICKET_PRICE)

# 11. Electricity Bill Calculation
#     The electricity company charges ₹8 per unit.
#     WAP to accept the number of units consumed and calculate and display the total bill.
print("\n--- Q11 Electricity Bill ---")
RATE_PER_UNIT = 8
units = int(input("Enter units consumed: "))
print("Total electricity bill: ₹", units * RATE_PER_UNIT)

# 12. Shopping Discount
#     The store offers a 10% discount on the marked price.
#     WAP to accept the marked price, calculate the discount amount and final payable
#     amount, and display all three values.
print("\n--- Q12 Shopping Discount ---")
marked_price = float(input("Enter marked price: "))
discount = marked_price * 10 / 100
final_amount = marked_price - discount
print("Marked price   : ₹", marked_price)
print("Discount (10%) : ₹", discount)
print("Final payable  : ₹", final_amount)

# 13. Student Marks and Percentage
#     Five subjects, each out of 100 marks.
#     WAP to accept marks in all five subjects and calculate and display the total marks
#     and percentage.
print("\n--- Q13 Marks and Percentage ---")
s1 = float(input("Enter marks of subject 1: "))
s2 = float(input("Enter marks of subject 2: "))
s3 = float(input("Enter marks of subject 3: "))
s4 = float(input("Enter marks of subject 4: "))
s5 = float(input("Enter marks of subject 5: "))
total = s1 + s2 + s3 + s4 + s5
percentage = total / 500 * 100
print("Total marks:", total, "/ 500")
print("Percentage :", round(percentage, 2), "%")

# 14. Travel Distance and Fuel Cost
#     Mileage is 15 km per litre, and petrol costs ₹100 per litre.
#     WAP to accept the distance travelled and calculate and display the fuel required
#     and total fuel cost.
print("\n--- Q14 Fuel Cost ---")
MILEAGE = 15
PETROL_PRICE = 100
distance = float(input("Enter distance travelled (km): "))
fuel = distance / MILEAGE
cost = fuel * PETROL_PRICE
print("Fuel required :", round(fuel, 2), "litres")
print("Total fuel cost: ₹", round(cost, 2))
