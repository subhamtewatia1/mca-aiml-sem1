import numpy as np

numbers_list=[13,32,23,44,5]
numbers = np.array(numbers_list)
print(numbers)
print(type(numbers))

#approach 1 : via loops
results_list=[]
for num in numbers_list:
    results_list.append(num * 2)
print(results_list)
print(type(results_list))
#approach 2 : numpy way (vectorized -- no loop)
result_array = numbers *2
print(result_array)
print(type(result_array))
