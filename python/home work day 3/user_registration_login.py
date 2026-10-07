# ============================================================
# PROJECT : User Registration & Login System
# ------------------------------------------------------------
# Task    : Sabhi ko ye task aaj EOD tak complete karna hai.
#           Classes me jo sikhaya gaya hai usi se khud banana hai.
#
# Project kya karta hai?
#   Part 1 - Registration : n users banao, har user ka strong
#                           password check karke dictionary me save karo.
#                           Password galat ho to EXACT batao kya missing hai.
#                           Password strong ho to CONFIRM PASSWORD poocho,
#                           dono match hon tabhi user save karo.
#   Part 2 - Login        : username poocho, password ke 5 chances do,
#                           sahi hua to Access Granted, warna Access Denied.
#
# Concepts used (jo class me padhe):
#   dictionary, for loop, while loop, break, if / elif / else,
#   boolean flag (True / False), string methods (isupper, islower,
#   isdigit), len(), in, input(), int()
# ============================================================


# ============================================================
# PART 1 : REGISTRATION (naye users banana)
# ============================================================

users = {}
# users     -> ek variable (naam jisme data rakhte hain)
# =         -> assignment operator: right side ki value left wale variable me daalo
# {}        -> khaali dictionary. Dictionary = key : value ka jodaa
#              yahan key = username, value = password  ->  {"amit": "Abc@1234"}

n = int(input("How many users? "))
# input()   -> user se keyboard par kuch likhwata hai, hamesha STRING deta hai
# "How many users? " -> ye message screen par dikhega (prompt)
# int()     -> string ko integer (number) me badalta hai, "3" -> 3
# n         -> kitne users banane hain, wo number yahan save hua


for i in range(n):
    # for       -> loop: ek kaam ko baar-baar karna
    # i         -> loop variable, har round me 0, 1, 2 ... n-1 banta hai
    # in        -> "ke andar se" ek-ek value lo
    # range(n)  -> 0 se n-1 tak numbers deta hai, yaani loop n baar chalega
    # :         -> iske baad wala indented (andar khiska hua) code loop ka hissa hai

    username = input("Enter username: ")
    # username  -> is user ka naam, jo dictionary ki KEY banega

    while True:
        # while     -> loop jo tab tak chalta hai jab tak condition True hai
        # True      -> condition hamesha sach -> infinite loop
        #              isse bahar sirf "break" se niklenge (jab password sahi ho)

        password = input("Enter password (8 characters): ")
        # password  -> user ka likha password (string)

        valid = True
        # valid     -> "flag" variable (boolean: sirf True ya False)
        # shuru me maan lo password SAHI hai (True)
        # neeche koi bhi rule toota to isse False kar denge

        upper = 0       # upper   -> kitne CAPITAL letters (A-Z) hain, shuru me 0
        lower = 0       # lower   -> kitne small letters (a-z) hain
        number = 0      # number  -> kitne digits (0-9) hain
        special = 0     # special -> kitne special characters (@, #, $, ! ...) hain
        # har naye password ke liye ginti 0 se shuru karni hai,
        # isliye ye while loop ke ANDAR likhe hain

        for name in password:
            # for ... in password -> string ke har character par ek-ek karke chalo
            # name      -> current character, jaise "A", "b", "@", "5"
            #              (naam kuch bhi rakh sakte hain, jaise ch ya letter)

            if name.isupper():
                # if        -> agar condition sach hai to neeche wala code chalao
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

            else:
                # else      -> upar ki koi condition sach nahi hui
                #              na capital, na small, na digit -> special character
                special += 1

            valid = True
            # NOTE: ye line zaroori nahi hai - valid pehle se hi True hai
            #       (upar while ke andar set kiya tha). Hata bhi do to
            #       program same chalega.

        # ---------- Ab har rule ALAG-ALAG check karo ----------
        # Yahan "elif" nahi, har jagah "if" hai -> isliye SAARI
        # galtiyan ek saath dikhengi, sirf pehli wali nahi.

        if len(password) < 8:
            # len()     -> string ki length (kitne characters)
            # <         -> "less than" (chhota hai)
            print("Password must have at least 8 characters.")
            # print()   -> screen par message dikhata hai
            valid = False
            # rule toota -> flag False (password galat hai)

        if upper < 1:
            # 1 se kam capital letter = ek bhi capital nahi
            print("Password must have at least 1 uppercase letter.")
            valid = False

        if lower < 1:
            # ek bhi small letter nahi
            print("Password must have at least 1 lowercase letter.")
            valid = False

        if number < 1:
            # ek bhi digit nahi
            print("Password must have at least 1 number.")
            valid = False

        if special < 1:
            # ek bhi special character nahi
            print("Password must have at least 1 special character.")
            valid = False

        if valid:
            # if valid: -> koi rule nahi toota -> password strong hai
            #              ab user se password DOBARA likhwao (confirm karne ke liye)

            confirm_password = input("Confirm password: ")
            # confirm_password -> user ne password dobara likha, wo yahan save hua

            if confirm_password == password:
                # ==        -> dono password bilkul same hain kya?
                #              same hain -> user sahi hai, save kar do
                users[username] = password
                # users[username] = password -> dictionary me nayi entry:
                #                               key = username, value = password
                print("User created successfully!")
                break
                # break     -> while True loop se turant bahar niklo
                #              (password sahi mil gaya, ab dobara mat poochho)

            else:
                # dono password match nahi hue
                print("Passwords do not match.")
                valid = False
                # flag False -> neeche "enter again" wala message dikhega
                #               aur while loop fir se password poochega

        print("Please enter the password again.\n")
        # yahan tabhi pahunchenge jab break nahi hua:
        #   1) password strong nahi tha, ya
        #   2) confirm password match nahi hua
        # \n        -> new line: message ke baad ek khaali line

print(users)
# saare bane hue users ki dictionary dikhao
# jaise: {'amit': 'Abc@1234', 'ravi': 'Xyz#5678'}


# ============================================================
# PART 2 : LOGIN (username + password check, 5 chances)
# ============================================================

username = input('enter your username ')
# login ke liye username poocha

if username in users:
    # in        -> check karta hai ki ye KEY dictionary me hai ya nahi
    #              hai to True, nahi to False

    correct_password = users[username]
    # users[username] -> us username ki VALUE (yaani save kiya hua password) nikaalo
    # correct_password -> sahi password yahan rakh liya, compare karne ke liye

    entered = ""
    # entered   -> user jo password likhega wo yahan aayega
    # ""        -> khaali string, taaki while loop kam se kam ek baar chale

    i = 0
    # i         -> galat attempts ki ginti (counter), shuru me 0

    while entered != correct_password:
        # !=        -> "not equal to" (barabar nahi hai)
        #              jab tak likha password sahi password ke barabar nahi, loop chalta rahe

        entered = input("Enter Password: ")

        if entered != correct_password:
            i += 1
            # galat password -> attempt count 1 badhao
            print("Wrong Password,", 5 - i, "attempts remaining")
            # 5 - i     -> kitne chances bache hain (total 5)
            # ,         -> print me alag-alag cheezein space ke saath jodta hai

        if i == 5:
            # ==        -> "barabar hai kya?" (comparison). Dhyan do: = assign karta hai, == compare
            print("Access Denied")
            break
            # 5 galat attempts ho gaye -> loop se bahar, aur chance nahi

    if entered == correct_password:
        # loop ke baad check: sahi password se bahar aaye ya 5 galat se?
        print("Access Granted")

else:
    # username dictionary me mila hi nahi
    print("Username does not exist")


# ============================================================
# SAMPLE RUN (Test)
# ------------------------------------------------------------
# How many users? 1
# Enter username: amit
# Enter password (8 characters): abc
#   Password must have at least 8 characters.
#   Password must have at least 1 uppercase letter.
#   Password must have at least 1 number.
#   Password must have at least 1 special character.
#   Please enter the password again.
# Enter password (8 characters): Abc@1234
# Confirm password: Abc@1235
#   Passwords do not match.
#   Please enter the password again.
# Enter password (8 characters): Abc@1234
# Confirm password: Abc@1234                      -> User created successfully!
# {'amit': 'Abc@1234'}
# enter your username amit
# Enter Password: abc12                           -> Wrong Password, 4 attempts remaining
# Enter Password: Abc@1234                        -> Access Granted
# ============================================================



#Wap to accept a no to the user and check the no is even or not and
#accept the another check no is prime no or not
#Accept another no from the user and  to check non is palindrome or not
# accept another no and check the prime or not
#accept another no check the no is prime or not
#accept the another no and check palindrome or not
