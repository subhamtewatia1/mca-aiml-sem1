# Program 3 - Guided Practice: Trace Before You Run

for i in range(1, 3):           # i = 1, 2
    for j in range(1, 4):       # j = 1, 2, 3
        print("i=" + str(i) + ", j=" + str(j))
# Output (inner loop pura chalta hai, phir i badhta hai):
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# i=2, j=3
