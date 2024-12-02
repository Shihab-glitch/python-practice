# Problem 05 - Exam Permit based on Attendance

Held=int(input("Enter the No. of classes held : "))
Attended=int(input("Enter the No. of classes attended : "))
Attendance=(Attended/Held)*100

print("Your Attendance:",Attendance,"%")

if (Attendance>=75):
    print("You are allowed to sit in the exam")
else:
    print("Sorry! You are not allowed to sit in the exam")