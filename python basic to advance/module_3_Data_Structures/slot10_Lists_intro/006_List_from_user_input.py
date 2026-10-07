# Program 5 - Independent Task: List from User Input

marks = []                          # khaali list
for i in range(5):                  # 5 baar input
    m = int(input("Enter mark: "))  # input: 70, 85, 60, 95, 80
    marks.append(m)                 # append -> list ke end me add

print("All marks:", marks)          # Output: All marks: [70, 85, 60, 95, 80]
print("Highest:", max(marks))       # Output: Highest: 95
print("Lowest:", min(marks))        # Output: Lowest: 60
