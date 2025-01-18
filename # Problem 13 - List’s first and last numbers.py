# If the list’s first and last numbers are the same

a = [int(x) for x in input("Enter the elements : ").split()]
print("Input list:", a)

if a[0] == a[-1]:
    print("True")
else:
    print("False")