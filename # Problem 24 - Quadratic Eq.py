# Problem 24 - Quadratic Equation

import math

a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))
d = b**2-4*a*c
if d > 0 :
    r1 = (-b+math.sqrt(d))/(2*a)
    r2 = (-b-math.sqrt(d))/(2*a)
    print("The Roots are :", r1,r2)
elif d == 0 :
    r1 = -b/(2*a)
    print("The Roots are :", r1)
else :
    print("The Roots are Imaginary")
print("The Equation is :", f"({a})x^2 + ({b})x + {c}")
print("The Discriminant is :", d)