# Exercises 1 : Rewrite your pay computation to give the employee 1.5 times the hourly rate 
# for hours worked above 40 hours

# Since the input("Enter the hour: ") and input("Enter your rate: ") are String
# However at pay = hours * rate , we are trying to do math , 
# so we need to declear float or int at hours and rate
# FYI : float in pythan is same as double in java

# hours = int(input("Enter the hour: "))
hours = float(input("Enter the hour: "))
rate =  float(input("Enter your rate: "))
overtime = 1.5

# Unlike in Java we need to use braces { } , in Python just use Colon :
if (hours >= 40) :
    pay = hours * rate * overtime
else : 
    pay = hours * rate
print("Pay: " , pay)