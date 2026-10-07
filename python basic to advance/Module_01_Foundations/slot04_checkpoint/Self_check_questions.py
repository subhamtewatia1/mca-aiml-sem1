# slot 04 - Self-Check Questions (Post-Lecture)

# Q1. List the six steps of the problem-solving framework in order.
# Ans: 1. Understand  - what is the input, what is the output
#      2. Break down  - split the problem into small steps
#      3. Plan        - write pseudocode in plain English
#      4. Code        - convert the plan into Python
#      5. Test        - run with normal and edge-case inputs
#      6. Reflect     - debug, fix and improve the code

# Q2. What is the difference between a syntax error and a logic error? Give one example of each.
# Ans: Syntax error -> the code breaks Python's grammar rules, so it does not run at all.
#      Logic error  -> the code runs without crashing, but gives the wrong answer.
# Syntax error example:
# print("Hello)                 # SyntaxError: closing quote is missing
# Logic error example:
a, b, c = 80, 90, 70
wrong_average = a + b + c / 3   # runs, but gives 193.33 because / happens before +
right_average = (a + b + c) / 3 # 80.0
print(wrong_average, right_average)

# Q3. Why is pseudocode written in English instead of Python?
# Ans: Pseudocode is for thinking about the LOGIC first, without worrying about syntax
#      (quotes, brackets, colons). Plain English is easy to read and fix, anyone can
#      understand it, and it can later be written in any programming language.

# Q4. In the marks-average program, what edge case should be tested besides normal input?
# Ans: - all marks 0          -> average should be 0.0
#      - all marks 100        -> average should be 100.0
#      - text like "abc"      -> int() gives ValueError
#      - negative or >100     -> program still accepts it, which is wrong
#      - decimal like 85.5    -> int() gives ValueError, float() would be needed

# Q5. A program runs without crashing but gives the wrong average. What type of error is
#     this, and how would you locate it?
# Ans: It is a LOGIC error.
#      To locate it:
#      - test with simple values where you already know the answer (80, 90, 70 -> 80.0)
#      - print the middle values (total, count) to see where it goes wrong
#      - check the formula: are all subjects added? are brackets used before dividing?
#      - compare the code line by line with the pseudocode plan
