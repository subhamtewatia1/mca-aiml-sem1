# Program 2 - Remove and Traverse

students = ["Alice", "Charlie", "Bob"]
students.remove("Charlie")          # value se hatao (index se nahi)
print(students)                     # Output: ['Alice', 'Bob']

for student in students:            # har element ek-ek karke
    print(student)                  # Output: Alice
                                    #         Bob
