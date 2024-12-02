# Problem 03 - Grading Marks

M=float(input("Enter your Marks : "))

if(M<25):
    print(" Grade F")
elif(M>=25 and M<45):
    print(" Grade E")
elif(M>=45 and M<50):
    print(" Grade D")
elif(M>=50 and M<60):
    print(" Grade C")
elif(M>=60 and M<80):
    print(" Grade B")
else:
    print(" Grade A")