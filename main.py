# Main File.
import pickle, time
from npc import *

# Main Game File for gemhunter
# TODO: puzzles, more mpcs, more content,  NPC's that can grant keys

#~/ Rooms \~#
roomFile = open('bin.dat', 'rb')
roomFile.seek(0)

class Room: # stores attributes of each room
    name = None   # Room num
    item = None   # str
    door = None   # str -> int
    up = None     # room
    down = None   # room
    left = None   # room
    right = None  # room
    NPC = None    # str


rooms = pickle.load(roomFile)

# Intro to Game
Introduction()

# Set Player location.
Player.room = rooms[0]

#~/ Main Loop \~#
while 1:
    InfoMessages()

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
            if room.name == keystrokes[travelTo]:
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
                        TypeOut("The door remains locked.")
                        time.sleep(1)
                else: # if there is not a door
                    Player.room = room


    # Menu
    else:
        ClearConsole()
        print("Menu:\n1. Search Room." # prints a menu of options
            "\n2. Open Inventory.\n"
        )
        menuOption = input("-> ")

        # Search Room
        if menuOption == "1":
            LoadingBar() 
            #Room Items.
            if Player.room.item: # if there is a item in the room
                TypeOut("You found a..",0.06, newline=False); ColorPrint(" %s!\n\n"%Player.room.item, TextColor.yellow)
                Player.inventory.append(Player.room.item)
                time.sleep(2)

            else:  # if there is not an item
                TypeOut("There aren't any items in this room..")
                time.sleep(1.5)

            # Room NPCs.
            if Player.room.NPC: # if there is an npc in the room
                TypeOut("You found..",0.06,newline=False); ColorPrint(" %s!\n\n"%Player.room.NPC, TextColor.yellow)
                time.sleep(2)

                interact = ValidInput("Would you like to interact with %s? (y/n)\n-> "%Player.room.NPC, "y","n")

                if interact == "y":
                    npc[Player.room.NPC]()

                else:
                    TypeOut("%s sadly sits alone."%Player.room.NPC)
                    time.sleep(1.5)

            else:  # if there is not an npc
                TypeOut("There aren't any NPCs in this room..")
                time.sleep(1.5)


        # Inspect inventory items.
        elif menuOption == "2":
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

            items[Player.inventory[itemChoice-1]]() # passes item in dictionary

            input("\nPress any key to continue..")
