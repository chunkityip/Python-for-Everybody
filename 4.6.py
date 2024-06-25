# def means function in python

def computepay(hours , rate):

    try:
        CorrectHours = float(hours)
        Corectrate =  float(rate)
    except ValueError:
        print("Please enter number")
        exit()


    overtime = 1.5


    if (CorrectHours >= 40) :
        pay = CorrectHours * Corectrate * overtime
    else : 
        pay = CorrectHours * Corectrate
    print("Pay: " , pay)


hours = (input("Enter the hour: "))
rate =  (input("Enter your rate: "))
computepay(hours , rate)
