# Calculate the sum of all even numbers between 1 and N

sum_even = 0
d = 2
n = int(input("Enter the value of N : "))
while d <= n:
   sum_even += d
   d += 2
print("Sum of even numbers from 1 to", n, "is", sum_even)