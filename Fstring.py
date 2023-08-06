# F-String
'''
str1 = "There are "
str2 = 11
str3 = " players in each cricket team."

# print(str1 + str2 + str3)  # Type-Error: Cannot contactenate string with an int

# print( str1 + str(str2) + str3 )  # Not an efficient way to type cast for each string

# result = "{1}{0}{2}" .format(str1, str2, str3)  # format function is again not a good way to write stirngs

# print(result)


# We use fstring to deal with TypeCast and format function

resultf = f"{str1}{str2}{str3}"

print(resultf)
'''

# Quick-Quiz :)

name = "Qadeer"

dob = "2.7.2000"

print("My name is:" f" {name}", "and my DateOfBirth is:" f"{dob}")
print("My name is:", name, "and my DateOfBirth is:", dob)

print(f"My name is:", {name}, "and my dob is:", {dob})
