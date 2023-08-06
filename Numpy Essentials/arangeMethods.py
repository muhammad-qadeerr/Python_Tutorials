import numpy as np

# arange() are bascically array creating routines in numpy 
    # - It returns the intrger value in range start and end including the start and excluding the end value.

arr = np.arange(0,11)  # array from 0 to 10 excluding 11
print(arr)

# linspace method
# Syntax: np.linspace(start, end, noOFElements)
arr2 = np.linspace(0,5,100)
print(arr2)

arr3 = np.linspace(6,9,50)
print(arr3)