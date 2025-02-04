# Problem 26 - Find Integer from List

input = int(input("Enter an integer : "))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if input in lst:
    print("The ingteger is in the list. The index of the integer in the list is :", lst.index(input))
else:
    print("Not Found")