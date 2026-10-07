#wap to assign values in DDA of size 3*4 and whenever than are even add 3 to it and make it to odd there the data is odd then add in the 5  2 dimensional\
# wap to accept values in 2 DDA of size 4*2 matrix addition

dda = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(3):
    for j in range(4):
        dda[i][j] = int(input(f"Enter value for element at position ({i+1},{j+1}): "))

for i in range(3):
    for j in range(4):
        if dda[i][j] % 2 == 0:
            dda[i][j] += 3
        else:
            dda[i][j] += 5

print("Modified DDA:")
for row in dda:
    print(row)

# wap to accept values in 2 DDA of size 4*2 matrix addition


matrix1 = [[0, 0], [0, 0], [0, 0], [0, 0]]
matrix2 = [[0, 0], [0, 0], [0, 0], [0, 0]]

print("Enter values for the first matrix:")
for i in range(4):
    for j in range(2):
        matrix1[i][j] = int(input(f"Enter value for element at position ({i+1},{j+1}): "))

print("Enter values for the second matrix:")
for i in range(4):
    for j in range(2):
        matrix2[i][j] = int(input(f"Enter value for element at position ({i+1},{j+1}): "))

result = [[0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(4):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Result of matrix addition:")
for row in result:
    print(row)