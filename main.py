import pickle, time
from npc import *

# Main Game File for gemhunter
# TODO: puzzles, more mpcs, more content,  NPC's that can grant keys

#~/ Rooms \~#
roomFile = open('bin.dat', 'rb')
roomFile.seek(0)

class Room: # stores attributes of each room
    name = None # Room num
    item = None # str
    door = None # str -> int
    up = None   # room
    down = None # room
    left = None # room
    right = None # room
    NPC = None # str


rooms = pickle.load(roomFile)

# Intro to Game
Introduction()

# Initialize Player
Player.room = rooms[0]
Player.inventory = ["GFUEL"]


#~/ Main Loop \~#
while 1:
    ClearConsole()

    # Informational messages
    ColorPrint("LOCATION:", TextColor.blue)
    TypeOut("You are currently in ", 0.010,newline=False); ColorPrint(Player.room.name,TextColor.blue) # types out the name of color in blue
    ColorPrint("\nINVENTORY:", TextColor.blue)
    TypeOut("%s"%', '.join(Player.inventory),0.010)

    # location messages
    print("Where would you like to travel to?",end =''); ColorPrint(" (u/d/l/r/m)",TextColor.lightpurple)

    # Travel options
    roomIndex = rooms.index(Player.room)    #ignore the stupidly long and ugly print statement below, it will type out move locations in blue
    print("up:",color("Room %s,"%rooms[roomIndex].up, TextColor.blue),"down:",color("Room %s,"%rooms[roomIndex].down, TextColor.blue),"left:",color("Room %s,"%rooms[roomIndex].left, TextColor.blue),"right:",color("Room %s,"%rooms[roomIndex].right, TextColor.blue))


    # Players next location
    travelTo = ValidInput("-> ","u","d","l","r","m","menu")
    # Travel.
    if "m" not in travelTo:
        keystrokes = {
                'u' : rooms[roomIndex].up,
                'd' : rooms[roomIndex].down,
                'l' : rooms[roomIndex].left,
                'r' : rooms[roomIndex].right
            }
        for room in rooms:
            if room.name == "Room %s"%keystrokes[travelTo]:
                if room.door: # if there is a door
                    ClearConsole()

                    if type(key[room.door]) == list:
                        doorKeys = ', '.join(key[room.door])
                    else:
                        doorKeys = key[room.door]

                    TypeOut("There is a %s in your path.  It requires: %s.\nWould you like to open it? (y/n)"%(room.door, doorKeys))
                    openDoorInp = ValidInput("-> ","y","n")

                    if openDoorInp == "y":
                        opened = openDoor(key[room.door])
                        if opened:
                            Player.room = room
                        else:
                            break
                    else:
                        break
                else: # if there is not a door
                    Player.room = room


    # Menu
    else:
        ClearConsole()
        print("Menu:\n1. Search Room." # prints a menu of options
            "\n2. Open Inventory."
            "\n3. Exit/Save Game.\n"
        )
        menuOption = input("-> ") 

        # Search Room
        if menuOption == "1": # search room
            # credit 2 JayPay loading bar
            ClearConsole()

            LoadingBar()

            ClearConsole()

            if Player.room.item: # if there is a item in the room
                TypeOut("You found a..",0.06, newline=False); ColorPrint(" %s!\n\n"%Player.room.item, TextColor.yellow)

                Player.inventory.append(Player.room.item)

                time.sleep(2)

            else:  # if there is not an item
                TypeOut("There aren't any items in this room..")
                time.sleep(2)


            if Player.room.NPC: # if there is an npc in the room
                TypeOut("You found..",0.06,newline=False); ColorPrint(" %s!\n\n"%Player.room.NPC, TextColor.yellow)
                time.sleep(2)

                interact = ValidInput("Would you like to interact with %s? (y/n)\n-> "%Player.room.NPC, "y","n")

                if interact == "y":
                    npc[Player.room.NPC]()

                else:
                    TypeOut("%s sadly sits alone."%Player.room.NPC)

            else:  # if there is not an npc
                TypeOut("There aren't any NPCs in this room..")
                time.sleep(2)


        if menuOption == "2": # inspecting items in inventory
            ClearConsole()

            ColorPrint("\nINVENTORY:", TextColor.blue)
            for index,name in enumerate(Player.inventory):
                print("%g. %s"%(index+1, str(name)))

            TypeOut("\nWhich item do you want to inspect?\n",newline=False)


            digit_list = ["0","1","2","3","4","5","6","7","8","9"]
            while True: # gets index input of the items
                itemChoice = input("-> ")
                if itemChoice not in digit_list:
                    itemChoice = input("-> ")

                elif int(itemChoice) in range(1,len(Player.inventory)+1) and itemChoice in digit_list:
                    itemChoice = int(itemChoice)
                    break
            inspectItem = items[Player.inventory[itemChoice-1]] # passes item in dictionary

            if inspectItem == "Chair": #for some reason, calling the funct from a dictionary ruins the loop, so, removed chair function
                ClearConsole()

                useChair = ValidInput('This chair can teleport you to any room.. in STYLE.\nWould you like to use it?\n(y/n)\n\n-> ', "y", "n")
                if useChair == "y":
                    ClearConsole()
                    digit_list = ["0","1","2","3","4","5","6","7","8","9"]
                    while True:
                        ClearConsole
                        teleportLocation = input("What is the number of the room you want to travel to?\n-> ")

                        if teleportLocation not in digit_list:
                            teleportLocation = input("What is the number of the room you want to travel to?\n-> ")

                        elif teleportLocation in digit_list and int(teleportLocation) in range(0,len(rooms)):
                            teleportLocation = int(teleportLocation)
                            break

                        TypeOut('Type a valid answer or I will go to your house and kill your family %s.'%Player.name)
                        time.sleep(1)

                    for room in rooms: # teleports the player to his desired location
                        if room.name == "Room %s"%teleportLocation:
                            Player.room = room
                            Player.inventory.remove("PewDiePie 100M Edition Clutch Chair")
                            TypeOut("You have arrived!\n",0.06)
                            break
                else:
                    ClearConsole()
                    TypeOut("The chair will be waiting for you.")

            else: # if the item isnt the chair
                TypeOut(inspectItem)

            input("\nPress any key to continue..")


        if menuOption == "3": # save game
            with open("save.py","w") as saveFile:
                saveFile.write("%s\n"%str(Player.name))
                saveFile.write("%s\n"%str(Player.inventory))
            input("Saved your progress.")
            exit(1)
