# Problem 04 - Age Determination

P01=int(input("Enter the age of the First Person : "))
P02=int(input("Enter the age of the Second Person : "))
P03=int(input("Enter the age of the Third Person : "))

if (P01>P02 and P01>P03):
    print("The First Person is the oldest")
    if (P02<P03):
        print("The Second Person is the youngest")
    else:
        print("The Third Person is the youngest")
elif(P02>P01 and P02>P03):
    print("The Second Person is the oldest")
    if (P01<P03):
        print("The First Person is the youngest")
    else:
        print("The Third Person is the youngest")
elif
    print("The Third Person is the oldest")
    if (P01<P02):
        print("The First Person is the youngest")
    else:
        print("The Second Person is the youngest")
else : print("There is something wrong with your input")
