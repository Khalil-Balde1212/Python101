import random

player_name = ""
player_max_hp = 10;
player_cur_hp = 10;
player_weapon_dmg = 2;

print("Hello welcome to Dino Hunter")
print("What is your name?")
player_name = input()

print()
print()
print()
print("Hello " + player_name + "! Are you ready to fight dinosaurs? (type y or n)")
if(input() == "y"):
    gameStart = True
    print("Awesome let's get started")
else:
    gameStart = False
    print("Tough. See you never I guess")

#start the game
if(gameStart == True):
    print()
    print()
    print()
    print("As you set foot on Dinoland, the humidity of the jungle before you warms you as you enter the jungle")
    input("Press enter to continue...")
    print("\n\n\n")
    print("Walking into the jungle you see a waterfall. Next to it you see something rustling in the bushes")
    print("What do you do? (Answer with the number)")
    print(" 1. Investigate the waterfall")
    print(" 2. Continue down")

    choice = input()
    if(choice == "1"):
        print("You investigate the waterfall and you find a DEFINETLY JUST A NERF BLASTER AND NOTHING VIOLENT")
        print("Your attack increases to 2")
        input("Press enter to continue...")
    elif(choice == "2"):
        print("The waterfall is too dangerous so you continue forward")
        input("Press enter to continue...")

    #get attacked
    print("\n\n\n")
    print("As you continue through the foliage, you are suddenly attacked by a Compsagnathus!!!")
    input("Press enter to continue...")
    print("\n\n\n")
    print("The rest of this game is under development!")

    # we will do an example of combat during session 3

