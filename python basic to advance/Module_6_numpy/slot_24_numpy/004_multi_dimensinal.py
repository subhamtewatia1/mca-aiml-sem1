# multidimensional (2-D): two lists -> two rows
Size = int(input("enter the size of the array:"))  # CORRECT: no need to re-import numpy

lst = []
lst2 = []

for i in range(Size):
    lst.append(int(input("enter the number for row 1:")))
    lst2.append(int(input("enter the number for row 2:")))
    # CORRECT: removed `lst.append(no)` -> `no` is not defined here (NameError) and it duplicates input

arr = np.array([lst, lst2])  # CORRECT: pass a list of lists, np.array(lst, lst2) is invalid
print(arr)
print(arr.ndim)  # 2
print(arr.shape)  # (2, Size)