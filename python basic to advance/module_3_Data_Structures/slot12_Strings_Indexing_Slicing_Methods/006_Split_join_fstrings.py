# Program 3 - Guided Practice: Split, Join & f-strings

# Complete: split this sentence into words
sentence = "Python is fun to learn"
words = sentence.split()                # blank -> split | space par todta hai
print(words)                            # Output: ['Python', 'is', 'fun', 'to', 'learn']

# Complete: join this list back into a sentence
parts = ["Data", "Science", "rules"]
joined = " ".join(parts)                # blank -> " " (space se jodo)
print(joined)                           # Output: Data Science rules

# Complete: format this using an f-string
city = "Sohna"
temp = 34
print(f"The temperature in {city} is {temp} degrees.")  # Output: The temperature in Sohna is 34 degrees.
