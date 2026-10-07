# Program 4 - Independent Task: Job Eligibility Checker
# Build an eligibility checker for a job:
# Criteria: age >= 21, has a degree (True/False), experience >= 2 years
age = int(input("Enter age: "))
has_degree = input("Do you have a degree? (yes/no): ") == "yes"
experience = int(input("Years of experience: "))

# Nested version - tells the candidate exactly which criterion failed
if age >= 21:
    if has_degree:
        if experience >= 2:
            print("Eligible for the job")
        else:
            print("Not eligible: need at least 2 years of experience")
    else:
        print("Not eligible: a degree is required")
else:
    print("Not eligible: must be at least 21")

# Compound version - shorter, but only one message
if age >= 21 and has_degree and experience >= 2:
    print("Eligible for the job")
else:
    print("Not eligible")
