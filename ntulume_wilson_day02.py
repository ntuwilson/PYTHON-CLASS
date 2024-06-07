age =  65
if age > 18:
    print ("You are an adult")
elif age > 65:
    print("You are a senior citizen")

else: 
    print("You are a youth")

# Exercise

age = int(input("Enter your age: "))


if age <= 13:
    print("Your price is 1000 ")

elif age <= 23:
    print("You will pay 1500")

elif age <= 65:
    print("You pay 2000")

else:
    print("You pay 5000")


#Exercise 0
colorlist  = ["red", "green", "blue", "purple", "yellow"] 

i = 5
while i > 0:
    print (colorlist[i])
    i = i - 1