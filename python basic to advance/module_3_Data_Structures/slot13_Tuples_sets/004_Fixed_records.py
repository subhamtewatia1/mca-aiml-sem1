# Program 4 - Independent Task: Store Fixed Records as Tuples

students = [
    ("Alice", 22, "Mumbai"),
    ("Bob", 21, "Delhi"),
    ("Charlie", 23, "Pune"),
]

for student in students:
    name, age, city = student               # har tuple ko unpack kiya
    print(f"{name} ({age}) lives in {city}")
# Output:
# Alice (22) lives in Mumbai
# Bob (21) lives in Delhi
# Charlie (23) lives in Pune
