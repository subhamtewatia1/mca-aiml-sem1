# Program 4 - Key Delete Karna (del)

person = {'name': 'Subham ', 'age': 22}

# del person["Age"]             # KeyError: 'Age' -> keys case-sensitive hain, "Age" != "age"
del person["age"]               # Fix: sahi key "age" (small a)
print(person)                   # Output: {'name': 'Subham '}
