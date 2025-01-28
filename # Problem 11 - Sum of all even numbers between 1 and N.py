# Calculate the sum of all even numbers between 1 and N

sum_even = 0
d = 2
n = int(input("Enter the value of N : "))
while d <= n:
   sum_even += d
   d += 2
print("Sum of even numbers from 1 to", n, "is", sum_even)

# Basic Code to find sum of all even numbers between 1 and 100
sum_even = 0
for i in range(2, 101, 2):
    sum_even = sum_even + i
print("Sum of even numbers from 1 to 100 is", sum_even)
