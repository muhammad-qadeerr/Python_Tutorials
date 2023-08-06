# For_loop is applicable on lists, ranges etc

marks = [95, 96, 97, 98]

# for score in marks:
#     print(score)

# Append-Operation: Add element at the end

marks.append(100)

print(marks)

# for score in marks:
#     print(score)

# Insert-operation: Similarly we can insert element at any position

marks.insert(1, 120)
print(marks)


for score in marks:
    print(score)

# Check element in the list

print(120 in marks)  # returns true.
print(150 in marks)  # returns false.

# check lenght of the list and string we use len keywork

print(marks)
print(len(marks))

name = "Qadeer"
print(name)
print(len(name))

# Printing list with while loop

print(marks)

i = 0

while i < len(marks):
    print(marks[i])
    i = i + 1

# To clear all the list

marks.clear()

print(marks)   # Displays [] now.
