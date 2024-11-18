working_days = float(input("enter your working days"))
absent_days = float(input("enter the days you were absent "))
percentage = 100-((absent_days / working_days)*100)
print("your percentage is", percentage)
if percentage <= 75:
    print("You cannot enter exam")
elif percentage >75:
   print("you can enter the exam") 

