code = raw_input("16-digit code (NO DASHES): ")
keyInterval = input("Interval: ")
print "\n\n"

#find the key
rawKey = []
for i in range(0,16,keyInterval):
    rawKey.append(code[i])
KEY = "".join(rawKey)

print "Starting Code: ",code
print "Key is: ",KEY

keyLocation = -1 #determines place in key string
for i in code:
    #calculate plce in key string
    keyLocation += 1
    if keyLocation > 3:
        keyLocation = 0
    #convert character to Decimal
    xCoord = ord(i)
    #subtract 65 to get x location in grid
    xCoord -= 65
    #convert key character to Decimal
    yCoord = ord(KEY[keyLocation])
    #subtract 65 to get y location in grid
    yCoord -= 65
    print "(",xCoord,",",yCoord,")"