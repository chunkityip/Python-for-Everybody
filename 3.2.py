# try except in Python is same idea as exception handling in Java

hours = (input("Enter the hour: "))
rate =  (input("Enter your rate: "))

try:
    CorrectHours = float(hours)
    Corectrate =  float(rate)
except ValueError:
    print("Please enter number")
    exit()


overtime = 1.5


if (hours >= 40) :
    pay = CorrectHours * Corectrate * overtime
else : 
    pay = CorrectHours * Corectrate
print("Pay: " , pay)