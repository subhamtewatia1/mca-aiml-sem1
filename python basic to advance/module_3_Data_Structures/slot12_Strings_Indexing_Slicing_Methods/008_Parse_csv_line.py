# Program 5 - Independent Task: Parse a CSV-Style Line

record = "Rahul,22,Delhi"
parts = record.split(",")                   # comma par todo -> ['Rahul', '22', 'Delhi']
name = parts[0]                             # Rahul
age = parts[1]                              # 22 (abhi bhi string hai)
city = parts[2]                             # Delhi
print(f"Name: {name}, Age: {age}, City: {city}")  # Output: Name: Rahul, Age: 22, City: Delhi
