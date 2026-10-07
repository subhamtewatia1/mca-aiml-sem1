 e# slot 01 - Self-Check Questions (Post-Lecture)

# Q1. What are the three stages of the IPO model? Give one real-life (non-computer) example of it.
# Ans: IPO = Input -> Process -> Output
#      Input   : data that goes in
#      Process : work done on that data
#      Output  : result that comes out
#      Example (making tea):
#        Input   -> water, milk, tea leaves, sugar
#        Process -> boiling and mixing them
#        Output  -> a cup of tea

# Q2. What does input() return — a number or text? How do you know?
# Ans: input() always returns text (a string), even if the user types a number.
#      We can check it with type():
num = input("Enter a number: ")
print(type(num))        # <class 'str'>
#      Also "10" + "5" gives "105" (joined), not 15, which shows it is text.
#      To use it as a number we convert it: int(num) or float(num)

# Q3. Write one line of code that prints your name and age together in a single sentence.
# Ans:
print("My name is Subham Tewatia and I am 21 years old.")

# Q4. Why does print(Hello) (without quotes) cause an error, but print("Hello") does not?
# Ans: Without quotes Python thinks Hello is a variable name.
#      No variable called Hello exists, so it gives NameError: name 'Hello' is not defined.
#      With quotes, "Hello" is a string (text), so Python just prints it.
# print(Hello)          # NameError
print("Hello")          # Hello

# Q5. What is the difference between what print() does and what input() does?
# Ans: print() -> OUTPUT : shows a message/value on the screen.
#      input() -> INPUT  : shows a message, waits for the user to type something,
#                          and returns what they typed as a string.
#      print() gives information to the user, input() takes information from the user.
