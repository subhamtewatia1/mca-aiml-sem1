# Program 6 - Debug: Immutability & Method Errors

# Bug 1: Trying to change a string in place
name = "Alice"
# name[0] = "B"                 # TypeError: 'str' object does not support item assignment

# Bug 2: Forgetting string methods return a NEW string (don't modify in place)
text = "hello"
text.upper()                    # naya string banta hai par kahin save nahi hua
print(text)                     # Output: hello  (abhi bhi, "HELLO" nahi)

# FIXES
name = "Alice"
name = "B" + name[1:]           # Bug 1 fixed: naya string banao
print(name)                     # Output: Blice

text = "hello"
text = text.upper()             # Bug 2 fixed: result wapas text me daalo
print(text)                     # Output: HELLO
