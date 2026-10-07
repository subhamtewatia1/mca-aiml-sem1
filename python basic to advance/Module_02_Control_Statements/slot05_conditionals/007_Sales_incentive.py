# slot 05 - Program 7 — Sales Incentive

rate = int(input("Enter the rate:"))
qty = int(input("Enter the quantity:"))
total = qty * rate

if total > 0:
    print("Total sales is :", total)
    if total >= 100000:
        print("The total incentive collected is", (total * 0.1))
    elif total >= 70000 and total < 100000:
        print("The total incentive collected is", (total * 0.07))
    elif total >= 40000 and total < 70000:
        print("The total incentive collected is", (total * 0.04))
    elif total < 40000:    # sheet had "total > 40000", which can never run here
        print("The incentive collected is", (total * 0))
else:
    print("Something is not right")
