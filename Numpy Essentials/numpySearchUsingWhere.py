import numpy as np

arr  = np.array([1, 2, 3, 4,2,4,2,5,2])

x = np.where(arr == 2)   # returns the index where 2 in present
y = np.where(arr %2 !=0) 
print(x)
print('\n')
print(y)