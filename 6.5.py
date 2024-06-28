str = "X-DSPAM-Confidence: 0.8475"

# find method is to found the location with specific syntax
ipos = str.find(":") # ":" is at index 18 at str 

piece = str[ipos :]

print(ipos)
print(piece)