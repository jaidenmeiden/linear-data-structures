"""
Code used in the shell to create an array
instance and methods.
"""

from customArray import CustomArray

menu = CustomArray(5)
len(menu)
print(menu)

for i in range(len(menu)):
    menu[i] = i + 1
print(menu[0])
print(menu[2])
for item in menu:
    print(menu)

print("len:", menu.__len__())
print("str:", menu.__str__())
print("iter:", menu.__iter__())
print("getitem:", menu.__getitem__(2))
print("setitem:", menu.__setitem__(2, 100))
print("str:", menu.__str__())
print("getitem:", menu.__getitem__(2))
