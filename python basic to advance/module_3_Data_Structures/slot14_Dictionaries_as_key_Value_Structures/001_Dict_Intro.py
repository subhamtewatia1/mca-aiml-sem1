# Program 1 - Dictionary Create & Access

Student = {
    "name": "Subham ",
    'age': 22,
    "city": "Mumbai",
    "name": "vicky",            # same key dobara -> purani value "Subham " replace ho gayi
}
print(Student)                  # Output: {'name': 'vicky', 'age': 22, 'city': 'Mumbai'}
print(type(Student))            # Output: <class 'dict'>
# print(Student[0])             # KeyError: 0 -> dict me index nahi, key se access hota hai
print(Student['name'])          # Output: vicky
print(Student['age'])           # Output: 22
print(Student.keys())           # Output: dict_keys(['name', 'age', 'city'])  (sirf keys)
print(Student.values())         # Output: dict_values(['vicky', 22, 'Mumbai'])  (sirf values)
