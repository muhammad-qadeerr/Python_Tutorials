import numpy as np
#from scipy import stats

#  Mean: the average value
#  Mode: the most common value
#  Median: the middle value


arr = np.array([1,2,3,34,5,5,6,7,8,8,9, 5])
# for x in arr:
#    sum = sum + arr[x]

#Calculation of mean

mean = 1+2+3+34+5+5+6+7+8+8+9+5/12

print('Mean is: ', mean)

#also Numpy method to calculate mean

mean2 = np.mean(arr)

print('Mean by array method is: ', mean2)

s = np.sort(arr)
x = np.median(s)

print('Median is: ', x)

#calculation of mode

#print(stats.mode(arr))

# Calculation of statndard deviation   

print('Standard Deviation: ',np.std(arr))