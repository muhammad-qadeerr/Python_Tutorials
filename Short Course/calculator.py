# Lets build a calculator using python
# import math
# print(dir(math))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Following operation can be performed by our calculator (+ , - , * , / , %, **) ")
print("Press 1 for Addition (+)")
print("Press 2 for Subtraction (-)")
print("Press 3 for  Multiplication (*)")
print("Press 4 for Division (/)")
print("Press 5 for Remainder (%)")
print("Press 6 for Exponent (**)")
operation = int(input("Enter your choice: "))


if operation == 1:
    print("The Sum is: ", n1 + n2)
elif operation == 2:
    print("The Difference is: ", n1 - n2)
elif operation == 3:
    print("The Multiplication result is: ", n1 * n2)
elif operation == 4:
    # can be n1 // n2 when we dont need floating point
    print("The Division result is: ", n1 / n2)
elif operation == 5:
    print("The Remainder after division is: ", n1 % n2)
elif operation == 6:
    print("The Exponent is: ", int(n1 ** n2))
else:
    print("Invalid Choice!!!!")
