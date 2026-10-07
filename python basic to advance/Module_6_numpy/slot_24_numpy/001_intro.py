import numpy as np

numbers = np.array([1, 11])
print(numbers)
print(type(numbers))# <class 'numpy.ndarray'> n dimensional array

numbers_list=([1, 2, 3,4, 5, 6,7, 8, 9])
print(numbers_list)
print(type(numbers_list))


for i in numbers:
    print(i , end= "")
    print(numbers_list[i])
    print(type(i))
