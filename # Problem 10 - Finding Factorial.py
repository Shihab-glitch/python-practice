# Calculate the factorial of a given number N

fact = 1
i = 1
n = int(input("Enter Number: "))
 
if n < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    while i <= n:
        fact = fact*i
        i = i + 1
    print("The factorial of", n, "is", fact)