with open("mbox-short.txt") as text:
    
    for i in text:
        x = i.rstrip()
        print(i.upper())
