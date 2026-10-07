# Question 002_numpy_traersing.py - Calculator (def / function ka use karke)
# ------------------------------------------------------------
# SIX-STEP FRAMEWORK
#
# Step 1 - Problem samajho:
#   User se 2 numbers aur ek operator (+ - * /) lo.
#   Har operation ke liye ALAG function (def) banao
#   aur sahi function call karke answer dikhao.
#   User jab tak "no" na bole, calculator chalta rahe.
#
# Step 2 - Input kya hai?
#   num1, num2 -> float (decimal bhi ho sakte hain)
#   op         -> string ("+", "-", "*", "/")
#
# Step 3 - Output kya hai?
#   Result, jaise: 10.0 + 5.0 = 15.0
#
# Step 4 - Formula / logic:
#   +  -> a + b        -  -> a - b
#   *  -> a * b        /  -> a / b   (b == 0 ho to error message)
#
# Step 5 - Code likho (neeche)
#
# Step 6 - Test karo (sabse neeche SAMPLE RUN dekho)
# ------------------------------------------------------------


# ============================================================
# PART 1 : FUNCTIONS BANANA (def)
# ============================================================

def add(a, b):
    # def       -> naya function banane ka keyword
    # add       -> function ka naam
    # (a, b)    -> parameters: function ke andar aane wale 2 inputs
    # :         -> iske neeche ka indented code function ki body hai
    return a + b
    # return    -> answer wapas bhejo, jahan se function call hua tha


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        # 0 se divide nahi kar sakte -> Python ZeroDivisionError deta
        return "Error! 0 se divide nahi kar sakte."
    return a / b


def calculate(num1, op, num2):
    # ye function operator dekh kar sahi function call karta hai
    # ek function ke andar doosra function call karna bilkul normal hai
    if op == "+":
        return add(num1, num2)
    elif op == "-":
        return subtract(num1, num2)
    elif op == "*":
        return multiply(num1, num2)
    elif op == "/":
        return divide(num1, num2)
    else:
        return "Invalid operator! Sirf + - * / use karo."


# ============================================================
# PART 2 : MAIN PROGRAM (functions ko CALL karna)
# ============================================================
# NOTE: def likhne se function sirf BANTA hai, chalta nahi.
#       Chalane ke liye naam + () likh kar CALL karna padta hai.

while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    result = calculate(num1, op, num2)
    # calculate(...) -> function CALL. Jo return hua, wo result me aa gaya

    print(num1, op, num2, "=", result)

    again = input("Aur calculation karni hai? (yes/no): ")
    if again.lower() != "yes":
        # .lower()  -> "YES" / "Yes" ko bhi "yes" bana deta hai
        print("Calculator band. Thank you!")
        break


# ============================================================
# SAMPLE RUN (Test)
# ------------------------------------------------------------
# Enter first number: 10
# Enter operator (+, -, *, /): +
# Enter second number: 5
# 10.0 + 5.0 = 15.0
# Aur calculation karni hai? (yes/no): yes
# Enter first number: 8
# Enter operator (+, -, *, /): /
# Enter second number: 0
# 8.0 / 0.0 = Error! 0 se divide nahi kar sakte.
# Aur calculation karni hai? (yes/no): no
# Calculator band. Thank you!
# ============================================================
