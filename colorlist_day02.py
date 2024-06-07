colorlist  = ["red", "green", "blue", "purple", "yellow"] 

i = 4
while i >= 0:
    print (colorlist[i])
    i = i - 1

reversed_colorlist = colorlist[::-1]
# using a for loop
for color in reversed_colorlist:
    print(color)


# using while loop
i =  len(colorlist) - 1
print (i)

while i >= 0:
    print (colorlist[i])
    i = i - 1


