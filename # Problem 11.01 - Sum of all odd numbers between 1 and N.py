# Problem 11.01 - Calculate the sum of all odd numbers between 1 and N

sum_odd = 0
n = int(input("Enter the value of N : "))
d = 1
while d <= n:
   sum_odd += d
   d += 2
print("Sum of odd numbers from 1 to", n, "is", sum_odd)


# Basic Code to find sum of all odd numbers between 1 and 100
sum_odd = 0
for i in range(1, 101, 2):
    sum_odd = sum_odd + i
print("Sum of odd numbers from 1 to 100 is", sum_odd)
