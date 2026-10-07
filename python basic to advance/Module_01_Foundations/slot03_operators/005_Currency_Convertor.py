# slot 03 - currency convertor
# rupees to dollar

rate = 97      # 1 usd = 97 inr

rupees = float(input('Enter amount in rupees: '))
usd = rupees / rate
print(rupees, "inr = ", round(usd, 2), "usd")

# other way, dollar to rupees
dollars = float(input('Enter amount in dollars: '))
inr = dollars * rate
print(dollars, "usd = ", round(inr, 2), "inr")


# ================= Sheet program =================
# Program 5 — Independent Task: Unit Converter
# Rupees to USD converter (approx rate)
rupees = float(input("Enter amount in INR: "))
usd = rupees / 97.65
print(rupees, "INR =", round(usd, 2), "USD")
