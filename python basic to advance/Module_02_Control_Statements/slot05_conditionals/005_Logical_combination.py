# slot 05 - Program 5 — Independent Task: and / or Combination

# A user gets a loan only if they are employed AND have a credit score above 700

is_employed = input("Are you employed? (yes/no): ") == "yes"
credit_score = int(input("Enter credit score: "))

if is_employed and credit_score > 700:
    print("Loan approved")
else:
    print("Loan not rejected")    # as written on the sheet, should say "Loan rejected"
