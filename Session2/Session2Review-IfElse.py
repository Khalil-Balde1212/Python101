#if else statements are yes or no questions!
numEggs = 2

if(numEggs == 0):
    print("You need to buy eggs!")
else:
    print("You have " + str(numEggs) + " eggs!")


# elif() is like asking "If not, then check this instead"
colour = "green"
if(colour == "red"):
    print("Red like an apple!")
elif(colour == "blue"):
    print("Blue like the sky!")
elif(colour == "green"):
    print("This colour is awesome!!")