# Display numbers from a list divisible by 5

a = [int(x) for x in input("Enter the elements : ").split()]
print("Input list:", a)

new_list = []
for num in a:
    if num % 5 == 0:
        new_list.append(num)
print("Numbers divisible by 5: ", new_list)