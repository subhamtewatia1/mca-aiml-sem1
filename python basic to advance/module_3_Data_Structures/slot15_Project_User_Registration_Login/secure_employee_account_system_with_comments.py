# ============================================================
# PROJECT : Secure Employee Account Management System (SEAMS)
# ------------------------------------------------------------
# Project kya karta hai?
#   Stage 1 - Account Setup   : manager batata hai kitne employee
#                               accounts banane hain. Har employee se
#                               username, password, confirm password lo.
#   Stage 2 - Secure Password : password ke 6 rules check karo.
#                               Ek bhi rule toota to "Password rejected!"
#                               aur EXACT batao kya missing hai.
#                               Password sahi ho to confirm password poocho.
#   Stage 3 - Employee Login  : username + password poocho, 5 chances do,
#                               sahi hua to Login successful, warna Access Denied.
#
# Concepts used (jo class me padhe):
#   dictionary, for loop, while loop, break, if / elif / else,
#   nested if, boolean flag (True / False), string methods (isupper,
#   islower, isdigit), len(), in, and, input(), int()
# ============================================================


# ============================================================
# STAGE 1 : ACCOUNT SETUP (naye employee accounts banana)
# ============================================================

users = {}
# users     -> ek variable (naam jisme data rakhte hain)
# =         -> assignment operator: right side ki value left wale variable me daalo
# {}        -> khaali dictionary. Dictionary = key : value ka jodaa
#              yahan key = username, value = password  ->  {"employee01": "Employee@123"}

print("===== SECURE EMPLOYEE ACCOUNT SYSTEM =====")

n = int(input("Enter number of accounts to create: "))
# input()   -> user se keyboard par kuch likhwata hai, hamesha STRING deta hai
# int()     -> string ko integer (number) me badalta hai, "2" -> 2
# n         -> kitne accounts banane hain, wo number yahan save hua


for i in range(n):
    # for       -> loop: ek kaam ko baar-baar karna
    # i         -> loop variable, har round me 0, 1, 2 ... n-1 banta hai
    # range(n)  -> 0 se n-1 tak numbers deta hai, yaani loop n baar chalega

    print("\n--- Account", i + 1, "---")
    # i + 1     -> i 0 se shuru hota hai, isliye 1 jodo taaki "Account 1" dikhe
    # \n        -> new line: heading se pehle ek khaali line

    username = input("Enter username: ")
    # username  -> is employee ka naam, jo dictionary ki KEY banega

    while username in users:
        # in        -> check karta hai ki ye username pehle se dictionary me hai ya nahi
        #              hai to naya username poocho, warna purana account overwrite ho jayega
        print("Username already exists. Please choose another username.")
        username = input("Enter username: ")

    password = input("Enter password: ")
    # password  -> employee ka likha password (string)
    # pehli baar password loop ke BAHAR poocha, taaki dobara poochte waqt
    # "Enter password again:" dikha sakein


    # ========================================================
    # STAGE 2 : SECURE PASSWORD CREATION (6 rules check)
    # ========================================================

    while True:
        # while     -> loop jo tab tak chalta hai jab tak condition True hai
        # True      -> condition hamesha sach -> infinite loop
        #              isse bahar sirf "break" se niklenge (jab account ban jaye)

        valid = True
        # valid     -> "flag" variable (boolean: sirf True ya False)
        # shuru me maan lo password SAHI hai (True)
        # neeche koi bhi rule toota to isse False kar denge

        upper = 0       # upper   -> kitne CAPITAL letters (A-Z) hain, shuru me 0
        lower = 0       # lower   -> kitne small letters (a-z) hain
        number = 0      # number  -> kitne digits (0-9) hain
        special = 0     # special -> kitne special characters (@, #, $, ! ...) hain
        space = 0       # space   -> kitne space (" ") hain
        # har naye password ke liye ginti 0 se shuru karni hai,
        # isliye ye while loop ke ANDAR likhe hain

        for name in password:
            # for ... in password -> string ke har character par ek-ek karke chalo
            # name      -> current character, jaise "E", "m", "@", "1"

            if name.isupper():
                # .isupper()-> string method: character CAPITAL hai to True
                upper += 1
                # +=        -> upper = upper + 1 ka short form (1 badhao)

            elif name.islower():
                # elif      -> "else if": upar wali condition jhoothi thi, ab ye check karo
                # .islower()-> character small letter hai to True
                lower += 1

            elif name.isdigit():
                # .isdigit()-> character 0-9 me se hai to True
                number += 1

            elif name == " ":
                # ==        -> character space hai kya?
                #              space ko special character NAHI ginna, isliye alag check
                space += 1

            else:
                # else      -> na capital, na small, na digit, na space -> special character
                special += 1

            valid = True
            # NOTE: ye line zaroori nahi hai - valid pehle se hi True hai
            #       (upar while ke andar set kiya tha). Hata bhi do to
            #       program same chalega.

        # ---------- Ab har rule ALAG-ALAG check karo ----------
        # Yahan "elif" nahi, har jagah "if" hai -> isliye SAARI
        # galtiyan ek saath dikhengi, sirf pehli wali nahi.
        #
        # Har rule ke andar "if valid:" (nested if) hai:
        #   valid abhi bhi True hai = ye PEHLI galti mili hai
        #   -> sabse pehle ek baar "Password rejected!" dikhao

        if len(password) < 8:
            # len()     -> string ki length (kitne characters)
            if valid:
                print("Password rejected!")
            print("Password must contain at least 8 characters.")
            valid = False
            # rule toota -> flag False (password galat hai)

        if upper < 1:
            # 1 se kam capital letter = ek bhi capital nahi
            if valid:
                print("Password rejected!")
            print("Password must contain at least one uppercase alphabet.")
            valid = False

        if lower < 1:
            # ek bhi small letter nahi
            if valid:
                print("Password rejected!")
            print("Password must contain at least one lowercase alphabet.")
            valid = False

        if number < 1:
            # ek bhi digit nahi
            if valid:
                print("Password rejected!")
            print("Password must contain at least one digit.")
            valid = False

        if special < 1:
            # ek bhi special character nahi
            if valid:
                print("Password rejected!")
            print("Password must contain at least one special character.")
            valid = False

        if space > 0:
            # ek bhi space mila -> rule toota
            if valid:
                print("Password rejected!")
            print("Password must not contain any space.")
            valid = False

        if valid:
            # if valid: -> "if valid == True:" ka short form
            #              koi rule nahi toota -> password strong hai
            #              ab password DOBARA likhwao (confirm karne ke liye)

            confirm_password = input("Confirm password: ")
            # confirm_password -> user ne password dobara likha, wo yahan save hua

            while confirm_password != password:
                # !=        -> "not equal to" (barabar nahi hai)
                #              jab tak dono match na hon, sirf confirm password dobara poocho
                print("Passwords do not match. Please enter the confirm password again.")
                confirm_password = input("Confirm password: ")

            users[username] = password
            # users[username] = password -> dictionary me nayi entry:
            #                               key = username, value = password
            print("Account created successfully!")
            break
            # break     -> while True loop se turant bahar niklo
            #              (account ban gaya, ab dobara mat poochho)

        password = input("Enter password again: ")
        # yahan tabhi pahunchenge jab valid False tha (break nahi hua)
        # naya password lo, while loop fir se saare rules check karega

print(users)
# saare bane hue accounts ki dictionary dikhao
# jaise: {'employee01': 'Employee@123', 'employee02': 'Secure#456'}


# ============================================================
# STAGE 3 : EMPLOYEE LOGIN (username + password, 5 chances)
# ============================================================

print("\n===== EMPLOYEE LOGIN =====")

i = 0
# i         -> galat attempts ki ginti (counter), shuru me 0

while i < 5:
    # <         -> jab tak 5 galat attempts nahi hue, loop chalta rahe

    username = input("Enter username: ")
    entered = input("Enter password: ")
    # entered   -> user ne jo password likha

    if username in users:
        # in        -> check karta hai ki ye KEY dictionary me hai ya nahi

        correct_password = users[username]
        # users[username] -> us username ki VALUE (yaani save kiya hua password) nikaalo

        if entered == correct_password:
            # nested if -> username sahi hai, ab password bhi sahi hai kya?
            # ==        -> "barabar hai kya?" (comparison)
            print("Login successful!")
            print("Welcome", username)
            break
            # login ho gaya -> loop se bahar

    i += 1
    # yahan tabhi pahunchenge jab username ya password galat tha
    # galat attempt -> count 1 badhao
    print("Invalid username or password.")

    if i < 5:
        # abhi chances bache hain -> kitne bache wo dikhao
        print("Attempts remaining:", 5 - i)
        # 5 - i     -> kitne chances bache hain (total 5)

if i == 5:
    # loop ke baad check: 5 galat attempts se bahar aaye?
    print("Access Denied!")
    print("Maximum login attempts exceeded.")


# ============================================================
# SAMPLE RUN (Test)
# ------------------------------------------------------------
# ===== SECURE EMPLOYEE ACCOUNT SYSTEM =====
# Enter number of accounts to create: 2
#
# --- Account 1 ---
# Enter username: employee01
# Enter password: abc123
#   Password rejected!
#   Password must contain at least 8 characters.
#   Password must contain at least one uppercase alphabet.
#   Password must contain at least one special character.
# Enter password again: Employee@123
# Confirm password: Employee@12
#   Passwords do not match. Please enter the confirm password again.
# Confirm password: Employee@123
#   Account created successfully!
#
# --- Account 2 ---
# Enter username: employee02
# Enter password: Secure#456
# Confirm password: Secure#456
#   Account created successfully!
# {'employee01': 'Employee@123', 'employee02': 'Secure#456'}
#
# ===== EMPLOYEE LOGIN =====
# Enter username: employee01
# Enter password: wrong123
#   Invalid username or password.
#   Attempts remaining: 4
# Enter username: employee01
# Enter password: Employee@123
#   Login successful!
#   Welcome employee01
# ============================================================
