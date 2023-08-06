import numpy as np

arr = np.array([3,4,5,6,7,8,9])

filter = arr%2 == 0     # it creates a boolean index at the backend and return the value acc to True in that index
print (filter)
newArr = arr[filter]

print(newArr)

print('\n\n')

arr2 = np.array([1,2,3,4,5,6,7])

filter = []  # Created a filter to put boolean index acc tp condition in it

for ele in arr: 
    if(ele % 2 == 0):
        filter.append(True)
    else: 
        filter.append(False)


newArr = arr2[filter]
print(newArr)