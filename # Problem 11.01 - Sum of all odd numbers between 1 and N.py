# Calculate the sum of all odd numbers between 1 and N

sum_odd = 0
n = int(input("Enter the value of N : "))
d = 1
while d <= n:
   sum_odd += d
   d += 2
print("Sum of odd numbers from 1 to", n, "is", sum_odd)
