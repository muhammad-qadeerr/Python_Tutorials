import numpy as np

# Search Sorted methods perform binary search in array assuming that array is sorted already


arr = np.array([1, 2, 3, 4,6,7,8])

x = np.searchsorted(arr, 6)

# performing the search form the right side  

y = np.searchsorted(arr, 7, side = 'right')

print('Element present at index: ', x)
print('Element present at index from right side: ', y)

print('\n')
# if given a unsorted arra we need to sort it first and then search in it


arr2 = ([3,2,6,4,1,56,78,43,23])

a = np.sort(arr2)
 
print(a)

z = np.searchsorted(a, 6)

print('Value present after sorting at: ', z)


