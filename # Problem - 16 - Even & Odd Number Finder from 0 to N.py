## Odd-Even Count

n = int(input("Enter N : "))
count_odd = 0
count_even = 0

for x in range(1, n + 1):
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1

print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)
