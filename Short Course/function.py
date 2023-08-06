# Three types of functions
# 1- Build-In Function
# 2- Module Function
# 3- User-Defined Function


# 1- Built-in functions are language defined functions as int(), input(), print() and  so on -----

# 2- Module functions: For Specific operations


import math

print(dir(math))


# Importing specific functions from library

from math import log

print(log(10))


# Importing all function we use staric

from math import *

print(sqrt(16))

# 3- User defined Functions

# Syntax   :  def function_name (parameter) : 

# Defining a function
def multiply_num (num1, num2, num3):
    print(num1 * num2 * num3)
    
# Calling a function

multiply_num(2, 3, 4)    



 