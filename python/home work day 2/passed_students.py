# Program 3 - Teacher se n students ke naam aur marks lo, phir
#             sirf pass hone wale students ke naam dikhao
# ------------------------------------------------------------
# SIX-STEP FRAMEWORK
#
# Step 1 - Problem samajho:
#   Teacher pehle batayega class me kitne student hain (n).
#   Uske baad har student ka naam aur uske marks poochne hain.
#   Aakhir me sirf un students ke naam print karne hain jo
#   exam pass kar gaye.
#
# Step 2 - Input kya hai?
#   n     -> int   (kitne students hain)
#   name  -> str   (har student ka naam)
#   mark  -> float (har student ke marks)
#
# Step 3 - Output kya hai?
#   Pass hone wale students ki list (naam + marks)
#
# Step 4 - Formula / logic:
#   PASS_MARK = 33  -> isse zyada ya barabar = pass
#   n baar loop chalao, har baar name aur mark input lo.
#   Dono ko parallel (saath-saath) do alag list me store karo:
#       names[0] ka mark marks[0] par milega, names[1] ka marks[1] par...
#   Phir dobara loop chala ke jiska mark >= 33 hai uska naam print karo.
#
#   NOTE: "parallel lists" ka matlab - do list, same index par
#   same student ka data. Isliye dono me append saath me karna hai.
#
# Step 5 - Code likho (neeche)
#
# Step 6 - Test karo:
#   n=3  Amit 75, Ravi 20, Sita 33
#        -> Pass: Amit (75), Sita (33)   | Ravi fail
#   n=2  Rahul 10, Neha 5
#        -> koi pass nahi
# ------------------------------------------------------------

PASS_MARK = 33                        # pass hone ke liye minimum marks

n = int(input("Enter how many students: "))

names = []                            # sab students ke naam
marks = []                            # sab students ke marks (same index)

# ---------- Input wala loop ----------
for i in range(n):
    print("\nStudent", i + 1)
    name = input("  Enter name: ")
    mark = float(input("  Enter mark: "))

    names.append(name)                # dono list me saath-saath daala
    marks.append(mark)                # taaki index match karta rahe

# ---------- Output wala loop ----------
print("\n----- Passed Students -----")

pass_count = 0                        # kitne pass hue, ginti ke liye

for i in range(len(names)):           # len(names) = total students
    if marks[i] >= PASS_MARK:
        print(names[i], "-", marks[i], "marks")
        pass_count = pass_count + 1

if pass_count == 0:
    print("Sorry, koi bhi student pass nahi hua.")
else:
    print("\nTotal passed =", pass_count, "out of", n)
