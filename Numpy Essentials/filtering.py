import numpy as np

#Filternig:  used to extract values from the sequence under certain conditions.

arr = np.array([False, False, True, False, False, True])

arr2 = np.array([1,2,4,5,6,7])

new = arr2[arr]

print(new )  # returns the ture value according to boolean array.


# Another filtering method using lambda function

seq = [2,3,4,5,6,67,7,8]

e = list(filter(lambda num: num%2 ==0, seq))      # it filters out the even from the seq
o = list(filter(lambda num: num%2 !=0, seq))      # it filters out the odd from the seq

print('Evens are:', e)
print('odds are:',o)

