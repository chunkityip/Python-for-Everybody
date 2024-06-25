answer = 0

while True:
    userInput = input("Enter a number: ")
    if userInput == "done": 
        break

    try :
        setInteger = int(userInput)
    except ValueError:
        print("Incorrect type")
        continue
    
    answer = setInteger

print(answer)

