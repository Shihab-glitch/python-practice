# Problem 08 - Payment after Discount

Price=float(input("Enter the Price : "))

if Price>10000 :
    print("You got 20% Discount, You have to pay = ", (Price*(1-0.20)))
elif (Price<=10000 and Price>7000) :
    print("You got 15% Discount, You have to pay = ", (Price*(1-0.15)))
elif Price<=7000 :
    print("You got 10% Discount, You have to pay = ", (Price*(1-0.10)))