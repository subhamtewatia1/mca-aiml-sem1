# slot 03 - Self-Check Questions (Post-Lecture)

# Q1. Why does "22" + "5" not equal 27 in Python? What does it actually produce?
# Ans: Both are strings (because of the quotes), and + on strings JOINS them, it does not add.
#      So it produces "225". To get 27 we must convert them first.
print("22" + "5")               # 225
print(int("22") + int("5"))     # 27

# Q2. What is the difference between / and // when dividing 10 by 3?
# Ans: /  is normal division, always gives a float with the decimal part.
#      // is floor division, gives only the whole number part (rounded down).
print(10 / 3)       # 3.3333333333333335
print(10 // 3)      # 3

# Q3. Write an expression using and that checks if a person can vote
#     (age >= 18) and is registered (is_registered is True).
# Ans:
age = 20
is_registered = True
print(age >= 18 and is_registered)      # True, both conditions must be True

# Q4. Predict the output of print(10 + 5 * 2) and explain why, using operator precedence.
# Ans: Output is 20.
#      * has higher precedence than +, so 5 * 2 = 10 is done first, then 10 + 10 = 20.
#      (If we want the + first, use brackets: (10 + 5) * 2 = 30)
print(10 + 5 * 2)       # 20
print((10 + 5) * 2)     # 30

# Q5. What type does int(input(...)) return, and why is that conversion necessary?
# Ans: It returns an int.
#      input() always gives a string, even if the user types a number.
#      Without int(), maths would not work: "5" + 1 gives TypeError and "5" + "5" gives "55".
num = int(input("Enter a number: "))
print(type(num))        # <class 'int'>
print(num + 1)
