# Display characters present at an odd index number

x = str(input("Enter the word - "))
even_index = []
for i in range(0,len(x)):
    if i % 2 != 0:
        even_index.append(x[i])
print(even_index)
