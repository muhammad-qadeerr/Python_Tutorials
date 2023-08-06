import numpy as np

arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr,'\n\n')

np.random.permutation(arr)
print(arr,'\n\n')


arr2 = np.random.rand(8)
print(arr2, '\n\n')
x = np.sort(arr2)
print(x, '\n\n')
np.random.permutation(arr2)
print(x, '\n\n')

