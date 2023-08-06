
# print("Lets Learn how to take input from the user in python")


# name = input("What is your name? ")

# print("Name:", name)

# # Use type conversion here to solve the error because string can only be concatenated with string not an integer

# age = int(input("What is your age? "))

# print("Age:", age)

# # Exerxcise

# super_hero = input("What is your super hero name? ")

# print("Your Super Hero is", super_hero)


# old_age = int(input("Enter your old age: "))

# # Type error here type_cast on the above or below line to get rid of the error

# # new_age = int(old_age) + 5
# new_age = old_age + 5

# print("Your new age is: ", new_age)


# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))
first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

# It will contatenate two numbers taking them as a string
# sum = first_num + second_num
sum = int(first_num) + int(second_num)

print(f"The sum of {first_num} and {second_num} is: ", sum)