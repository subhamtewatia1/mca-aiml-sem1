#complete: print number 10,20,30....100

for i in range(10, 101, 10):
    print(i, end=', ' if i != 100 else '\n')

print(*range(10, 101, 10), sep=', ')

# complete: sum the number 1 to 50
total = 0
for i in range(1, 51):
    total = total + i
print("sum of 1 to 50 =", total)
