# Program 6 - Debug Workshop / Mutation Bugs

# Bug 1: remove() removes by VALUE, not index -- missing value par crash
students = ["Alice", "Bob"]
# students.remove("Charlie")        # ValueError: 'Charlie' list me hai hi nahi

# Bug 2: append() list ko badal deta hai aur None return karta hai
# students = students.append("Dave")  # WRONG: students ab None ban jata
# print(students)                     # Output: None

# FIXES
students = ["Alice", "Bob"]
if "Charlie" in students:           # Bug 1 fixed: pehle check karo
    students.remove("Charlie")      # yahan chalega hi nahi, koi crash nahi

students.append("Dave")             # Bug 2 fixed: bina reassign kiye call karo
print(students)                     # Output: ['Alice', 'Bob', 'Dave']
