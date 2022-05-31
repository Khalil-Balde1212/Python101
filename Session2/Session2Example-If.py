print("How many eggs did")
print("Gaston eat this morning?")

#Get how many eggs he ate
eggs = input()
eggs = int(eggs)

DOZEN_EGGS = 12 #this number represents how many eggs are in a


print("Gaston ate " + str(int(eggs/DOZEN_EGGS)) + " dozen eggs and " + str(eggs % DOZEN_EGGS) + " eggs")
print()

if(eggs >= 5 * DOZEN_EGGS):
    print("Gaston will be roughly")
    print("The size of a barge")

elif(eggs >= 4 * DOZEN_EGGS):
    print("Gaston will be large")

else:
    print("Gaston will not get large")
    print("Please give him more eggs :(")