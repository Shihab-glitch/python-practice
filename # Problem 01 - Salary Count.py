# Problem 01 - Bonus Calculation

Current_Salary = float(input("Enter your Current Salary: "))
yos = float(input("Enter your years of service: "))
if yos > 5:
   bonus = Current_Salary * 0.05
   print("Your net bonus is: ", bonus)
else:
   print("You're very young, dediacte a few more years to get the bonus.")