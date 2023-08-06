# Termination of programm is done by break/continue

marks = [95, 86, 89, 99, 95]
print(marks)

for score in marks:
    if score == 99:        # Python reads the value in sequence in the list
        break
    print(score)
    
    
# friends = ["Raheeb", "Bilal", "Qadeer", "Osama", "Uzair"]
# print(friends)

# for name in friends:
#     if name == "Qadeer":
#         break
#     print(name)


# Continue in python

friends = ["Raheeb", "Bilal", "Qadeer", "Osama", "Uzair"]
print(friends)

for name in friends:
    if name == "Qadeer":  # If Qadeer exculde it and continue the loop
        continue
    print(name)

