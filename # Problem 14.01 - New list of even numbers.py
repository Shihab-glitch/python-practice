# Display even numbers from a list

a = [int(x) for x in input("Enter the elements : ").split()]
print("Input list:", a)

new_list = []
for num in a:
    if num % 2 == 0:
        new_list.append(num)
print("Even numbers: ", new_list)
