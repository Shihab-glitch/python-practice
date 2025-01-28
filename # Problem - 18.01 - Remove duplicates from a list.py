# Problem - 18.01 - Remove duplicates from a list

# String Input
list = input("Enter the elements: ").split()
print("Original list:", list)
new_list = []
for num in list:
    if num not in new_list:
        new_list.append(num)
print("List without duplicates:", new_list)

# Integer Input
list = [int(x) for x in input("Enter the elements: ").split()]
print("Original list:", list)
new_list = []
for num in list:
    if num not in new_list:
        new_list.append(num)
print("List without duplicates:", new_list)
