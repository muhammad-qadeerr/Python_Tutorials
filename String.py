# Strings


# Single-line String

# Can be written in sigle of double quotation


name = "Qadeer"

print("My name is:", name)

# Multi-line String
# Multi-line Strings can be written using triple quotation Mark

intro = " I am a student of BSCS in University of Punjab College of Information and Technology Lahore."

print("My Short Introduction is:", name + "." + intro)

# String is bascically an Array

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Limit the Array

# These both are identical
print(name[:5])
print(name[:5])    # (0 - n-1 i.e there is null terminating char on the last)

# Before colon is starting idex and before is ending index
# We can limit is as we can i-e

print(name[1:4])


fresh = "   Python Programming   "

print("String Methods/Function")
print("Lenght of string is:", len(fresh))  # Space will be count

print(fresh.strip())   # Function help to print string with spaces

print(fresh.upper())   # Helps Convert the string into upper-case

print(fresh.lower())   # Helps print the string into lower-case

# Helps Replacing the String Charcters/Words
print(fresh.replace('Python', 'C++'))


n = "1,2,3,4,5,6,7,8,9"

print(n.split(" , "))   # Helps converting the number into Lists
