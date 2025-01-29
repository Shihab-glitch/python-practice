# Display characters present at an odd index number

x = str(input("Enter the word - "))
odd_index = []
for i in range(0,len(x)):
    if i % 2 != 0:
        odd_index.append(x[i])
print(odd_index)
