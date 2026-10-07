# Program 3 - Key Exist Karti Hai ya Nahi (in operator)

person = {'name': 'Subham ', 'age': 22}

if "city" in person:            # "in" sirf KEYS me check karta hai
    print(person['city'])
else:
    print("city not Found")     # Output: city not Found
