# Duplicate Checker

a = [int(x) for x in input("Enter the elements : ").split()]
print("Input list:", a)
s = set(a)
if len(s) != len(a):
    print("Duplicates found")
else:
    print("No duplicates found")