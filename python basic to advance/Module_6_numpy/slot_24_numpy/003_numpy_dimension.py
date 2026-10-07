# wap a program multiple values in a list and store it in a single Dimensional array display it
import numpy as np

Size = int(input("enter the size of the array:"))
lst = []
for i in range(Size):
    no = int(input("enter the number:"))
    lst.append(no)

arr = np.array(lst)  # CORRECT: np.array(lst, lst2) was wrong -> 2nd arg is dtype; 1-D needs only one list
print(arr)
print(arr.ndim)  # 1


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
