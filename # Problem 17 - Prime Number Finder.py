# Problem 17 - Prime Number Finder

from math import sqrt
n = int(input("Enter number to check: "))
prime = 0

if(n > 1):
    for i in range(2, (int(sqrt(n)) + 1)):
        if (n % i == 0):
            prime = 1
            break
    if (prime == 0):
        print("The number", n, "is a prime.")
    else:
        print("The number", n, "is not a prime.")
else:
    print("Wrong input. Please, enter a number greater than 1.")
