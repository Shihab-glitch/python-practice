P01=int(input("Enter the age of the First Person : "))
P02=int(input("Enter the age of the Second Person : "))
P03=int(input("Enter the age of the Third Person : "))

if P01<=0 and P02<=0 and P03<=0 :
    print("Wrong Input")
elif (P01>P02 and P01>P03):
    print("The First Person is the oldest")
    if (P02<P03):
        print("The Second Person is the youngest")
    elif (P03<P02):
        print("The Third Person is the youngest")
    elif (P02==P03):
        print("The Second & Third Person both are of same age")
elif (P02>P03 and P02>P01):
    print("The Second Person is the oldest")
    if (P01<P03):
        print("The First Person is the youngest")
    elif (P03<P01):
        print("The Third Person is the youngest")
    elif (P03==P01):
        print("The First & Third Person both are of same age")
elif (P03>P02 and P03>P01):
    print("The Third Person is the oldest")
    if (P02<P01):
        print("The Second Person is the youngest")
    elif (P01<P02):
        print("The First Person is the youngest")
    elif (P02==P01):
        print("The First & Second Person both are of same age")
elif P01==P02 and P02>P03 :
    print("The First and Second Person are of same age and older than The Third Person")
elif P03==P01 and P01>P02 :
    print("The First and Third Person are of same age and older than The Second Person")
elif P03==P02 and P02>P01 :
    print("The Second and Third Person are of same age and older than The First Person")
else : print("They are all of the same age")