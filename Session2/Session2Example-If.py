print("How many eggs did")
print("Gaston eat this morning? : ")

eggs = input()
eggs = int(eggs)

dozenEggs = 12

print("Gaston ate " + str(int(eggs/dozenEggs)) + " dozens and " + str(eggs % dozenEggs) + " eggs")
if(eggs >= 5*dozenEggs):
    print("Gaston will be roughly")
    print("The size of a barge")

elif(eggs >= 4*dozenEggs):
    print("Gaston will be large")

else:
    print("Gaston will not get large")
    print("Please give him more eggs :(")