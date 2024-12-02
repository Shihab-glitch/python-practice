# Problem 07 - Finding the largest number out of 3 inputs

N01=float(input("Enter the First Number : "))
N02=float(input("Enter the Second Number : "))
N03=float(input("Enter the Third Number : "))

if (N01>N02 and N01>N03) :
    print("The First Number is the Largest")
elif (N02>N03 and N02>N01) :
    print ("The Second Number is the Largest")
elif (N03>N01 and N03>N02) :
    print("The Third Number is the Largest")
else :
    print("There might be something wrong with your input")
