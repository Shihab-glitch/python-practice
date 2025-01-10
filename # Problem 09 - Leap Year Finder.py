# Problem 09 - Leap Year Finder

Y = int(input("Enter your year : "))

if Y % 100 == 0 :
    if Y % 400 == 0 :
        print("It's a Leap Year")
    else :
        print("It's not a Leap Year")
elif Y % 4 == 0 :
    print("It's a Leap Year")
else :
    print("It's not a Leap Year")
