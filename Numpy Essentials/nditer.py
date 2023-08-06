import numpy as np

# nditer function print the multidimensional array down to scalar easily

arr2 = ([[[1,2,3],[3,4,5],[3,4,5]]])

for x in np.nditer(arr2):
    print (x)