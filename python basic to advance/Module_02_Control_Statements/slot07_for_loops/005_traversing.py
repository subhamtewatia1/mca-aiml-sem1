#WAP to accept a word from the user and print every character on a new line
word = input("Enter a word: ")

for ch in word:
    print(ch)

print()

#WAP to print every character with its index
for i in range(len(word)):
    print(i, "->", word[i])

print()

#WAP to count the vowels in the word
vowels = 0
for ch in word:
    if ch.lower() in "aeiou":
        vowels += 1
print("Total vowels =", vowels)

#WAP to print the word in reverse
reverse = ""
for ch in word:
    reverse = ch + reverse
print("Reverse =", reverse)

#WAP to traverse a list of marks and print the total
marks = [45, 78, 62, 90, 55]
total = 0
for m in marks:
    total = total + m
print("Total marks =", total)
print("Average marks =", total / len(marks))
