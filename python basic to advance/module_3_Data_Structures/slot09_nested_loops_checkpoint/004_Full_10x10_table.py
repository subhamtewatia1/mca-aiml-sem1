# Program 4 - Independent Task: Full 10x10 Multiplication Table

for i in range(1, 11):          # rows: 1 se 10
    for j in range(1, 11):      # columns: 1 se 10
        print(i*j, end="\t")    # \t -> tab, columns seedhe rehte hain
    print()                     # har row ke baad nayi line
# Output:
# 1   2   3   4   5   6   7   8   9   10
# 2   4   6   8   10  12  14  16  18  20
# 3   6   9   12  15  18  21  24  27  30
# ...
# 10  20  30  40  50  60  70  80  90  100
