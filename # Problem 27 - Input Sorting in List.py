# Problem 27 - Input Sorting in List

lst = []
n = int(input("Enter the number of elements in the list : "))
for i in range(n):
    lst.append(int(input("Enter an element : ")))
lst.sort()
print("The ascending list is :", lst)

lst.sort(reverse = True)
print("The descending list is :", lst)