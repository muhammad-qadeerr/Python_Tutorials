import numpy as np 


# x = np.random.rand()   # Gives the random float value between 0 and 1
# print(x)

# print('\n')
# print('\n')

# Another method

from numpy import random

# y = random.rand(5)  #Generates 5 random numbers
# print(y)

# print('\n')
# print('\n')

# z = random.rand(5,6)  #Generates 5 random numbers
# print(z)


# x= random.randn()
# print(x)
# x= random.randn(4)
# print(x, '\n')
# x= random.randn(4,4)
# print(x, '\n')
# x= random.randn(4,4,5)
# print(x)



# randint() method - gives the random number in a range
#syntax np.random.randint(start,end)
# x = np.random.randint(1,10)
# print(x)
# x = np.random.randint(-4,5)
# print(x)


# Some Examples
#1 - CREATE a random array and sort it.

a = np.random.rand(6)
print(np.sort(a))

#2 - CREATE a random array of 2*3 with random no between 6 and 9

# b = np.random.randint(6,9,(2,3))
# print(b)


arr = np.random.randint(1,10000, size = 1000)
print(arr, '\n\n')
s = np.sort(arr)
print(s, '\n\n')

minElement = np.min(arr)
print(minElement, '\n\n')
maxElement = np.max(arr)
print(maxElement, '\n\n')

mean = np.mean(arr)
print(mean, '\n\n')

SD = np.std(arr)
print(SD, '\n\n')




