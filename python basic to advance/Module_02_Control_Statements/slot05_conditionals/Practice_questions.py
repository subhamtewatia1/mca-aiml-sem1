# slot 05 - Practice Questions
# (every question asks for input, so running the file asks them one after another)

# 1. WAP to accept a year and check whether the year is a leap year or not.
#    (If the year is divisible by 4, it is a leap year.)
print("\n--- Q1 Leap Year ---")
year = int(input("Enter a year: "))
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
# full rule: divisible by 4 and not by 100, OR divisible by 400 (1900 is not leap, 2000 is)
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:

# 2. WAP to accept two numbers and print the maximum number.
print("\n--- Q2 Maximum ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Maximum:", a)
elif b > a:
    print("Maximum:", b)
else:
    print("Both numbers are equal")

# 3. WAP to accept two numbers and print the minimum number.
print("\n--- Q3 Minimum ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print("Minimum:", a)
elif b < a:
    print("Minimum:", b)
else:
    print("Both numbers are equal")

# 4. WAP to accept the age of two people along with their names and print who between
#    them is elder and younger with proper statements.
print("\n--- Q4 Elder / Younger ---")
name1 = input("Enter first person's name: ")
age1 = int(input("Enter " + name1 + "'s age: "))
name2 = input("Enter second person's name: ")
age2 = int(input("Enter " + name2 + "'s age: "))
if age1 > age2:
    print(name1, "is elder and", name2, "is younger")
elif age2 > age1:
    print(name2, "is elder and", name1, "is younger")
else:
    print(name1, "and", name2, "are of the same age")

# 5. WAP to accept length and breadth from the user and display whether the given shape
#    is a square or a rectangle.
print("\n--- Q5 Square or Rectangle ---")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
if length == breadth:
    print("It is a square")
else:
    print("It is a rectangle")

# 6. WAP to accept the Cost Price (C.P.) and Selling Price (S.P.) of an article and calculate
#    whether there is a profit or loss, the profit/loss amount, and the profit/loss percentage.
print("\n--- Q6 Profit / Loss ---")
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
if sp > cp:
    profit = sp - cp
    print("Profit of ₹", profit)
    print("Profit % :", round(profit / cp * 100, 2), "%")
elif cp > sp:
    loss = cp - sp
    print("Loss of ₹", loss)
    print("Loss % :", round(loss / cp * 100, 2), "%")
else:
    print("No profit, no loss")

# 7. WAP to accept final percentage and display the division:
#    Above 85% -> Distinction, 60-85% -> First, 50-60% -> Second, 40-50% -> Third, Below 40% -> Fail
print("\n--- Q7 Division ---")
percentage = float(input("Enter final percentage: "))
if percentage > 85:
    print("Division: Distinction")
elif percentage >= 60:
    print("Division: First")
elif percentage >= 50:
    print("Division: Second")
elif percentage >= 40:
    print("Division: Third")
else:
    print("Division: Fail")

# 8. WAP to accept the sales of a salesman and calculate the commission:
#    ₹30,001 onwards -> 9%, ₹22,001-₹30,000 -> 7%, ₹12,001-₹22,000 -> 5%,
#    ₹5,001-₹12,000 -> 3%, Below ₹5,000 -> 0.5%
print("\n--- Q8 Commission ---")
sales = float(input("Enter sales amount: "))
if sales > 30000:
    rate = 9
elif sales > 22000:
    rate = 7
elif sales > 12000:
    rate = 5
elif sales > 5000:
    rate = 3
else:
    rate = 0.5
commission = sales * rate / 100
print("Commission rate:", rate, "%")
print("Commission: ₹", round(commission, 2))

# 9. WAP to accept the name of the owner, meter number, and units consumed and calculate
#    the electricity bill (JSEB tariff):
#    Up to 100 units -> ₹2.5/unit, Next 100 -> ₹3.5/unit, Next 100 -> ₹4/unit, Remaining -> ₹4.5/unit
#    Plus ₹100 Service Charge per month. Print the bill with owner name and meter number.
print("\n--- Q9 JSEB Electricity Bill ---")
SERVICE_CHARGE = 100
name = input("Enter the name of owner: ")
meter = input("Enter meter number: ")
units = int(input("Enter units consumed: "))
if units <= 100:
    energy = units * 2.5
elif units <= 200:
    energy = (100 * 2.5) + (units - 100) * 3.5
elif units <= 300:
    energy = (100 * 2.5) + (100 * 3.5) + (units - 200) * 4
else:
    energy = (100 * 2.5) + (100 * 3.5) + (100 * 4) + (units - 300) * 4.5
total_bill = energy + SERVICE_CHARGE
print("===== JSEB Electricity Bill =====")
print("Owner name     :", name)
print("Meter number   :", meter)
print("Units consumed :", units)
print("Energy charge  : ₹", energy)
print("Service charge : ₹", SERVICE_CHARGE)
print("Total bill     : ₹", total_bill)
