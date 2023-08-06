import numpy as np
# arr1 = np.array([1,2,3,4,5,8])   # 1D array

# # interating ther aray: 

# for i in arr1:
#     print(i)
# print('\n')

# # 2D array iteration

# arr2 = ([1,2,3],[3,4,5])

# for x in arr2:
#     print(x)

# print('\n')
# # 3D array iteration

# arr3 = np.array([[[1,2,3],[3,4,5]],[[1,2,3], [3,4,5]]])
# print(arr3)

# print('\n')

# for x in arr3:
#     print(x)



# ITERATION _ II - Nested loop for 2D arrays

arr2 = np.array([[1,2,3], [4,5,6]])

# printing scalar elements i.e iterating down to scalars
for x in arr2:
    for y in x:
        print(y)

print('\n')
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

for x in arr3:
    for y in x:
        for z in y:
            print(z)


