# wap to assign values in a 2D array of 3*4 Display
import numpy as np

rows = 3
cols = 4

arr_list = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(int(input(f"enter the number for [{r}][{c}]:")))
    arr_list.append(row)
# CORRECT: the old code asked for `Size` and used lst/lst2 with an undefined `no` (NameError);
# a 3*4 array needs 3 rows x 4 columns = 12 values, built row by row

arr = np.array(arr_list)  # CORRECT: np.array(lst, lst2) is invalid -> pass one list of lists
print(arr)
print(type(arr))  # <class 'numpy.ndarray'>
print(arr.shape)  # (3, 4)
print(arr.size)  # 12
print(arr.dtype)  # int64
print(arr.ndim)  # 2  (CORRECT: duplicate arr.shape print replaced with ndim)


#

matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
print(matrix+3)
print(type(matrix))
print(matrix.shape)
print(matrix.size)
print(matrix.ndim)