# Main Game File for gemhunter
from npc import *

# Intro to Game
# TODO: Uncomment this for production -> Introduction()

#~/ Main Loop \~#
while 1:
    InfoMessages()

    # Remove any doors that have been opened, or that the player may be trapped behind from teleporting.
    if Player.room.door:
        Player.room.door = None; Player.room.key = None

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
        room = rooms[keystrokes[travelTo]]

        if room.door:
            ClearConsole()

            doorKeys = ', '.join(room.door[2])

            TypeOut("There is a %s in your path.  It requires: %s.\nWould you like to open it? (y/n)"%(room.door[1], doorKeys))
            openDoorInp = ValidInput("-> ","y","n")

            if openDoorInp == "y":
                opened = openDoor(room.door[2], doorName=room.door[1])
                if opened:
                    Player.room = room
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
            ClearConsole()
            #Room Items.
            if Player.room.item: # if there is a item in the room
                TypeOut("You found a..",0.06, newline=False); ColorPrint(" %s!\n\n"%Player.room.item, TextColor.yellow)
                Player.inventory.append(Player.room.item)
                time.sleep(2)

            else:  # if there is not an item
                TypeOut("There aren't any items in this room..")
                time.sleep(1.5)

            # Room NPCs.            
            if Player.room.npc: # if there is an npc in the room
                TypeOut("You found..",0.06,newline=False); ColorPrint(" %s!\n\n"%Player.room.npc, TextColor.yellow)
                time.sleep(2)

                interact = ValidInput("Would you like to interact with %s? (y/n)\n-> "%Player.room.npc, "y","n")

                if interact == "y":
                    npc[Player.room.npc]()

                else:
                    TypeOut("%s sadly sits alone."%Player.room.npc)
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

            while True: # gets index input of the items
                try:
                    itemChoice = int(input("-> "))
                    if int(itemChoice) in range(0,len(Player.inventory)-1) or itemChoice == len(Player.inventory):
                        break
                except:
                    pass

            if "Tunnel" in Player.inventory[itemChoice-1]: # special case for tunnel, bc item name is different across players.
                items[Player.inventory[itemChoice-1][0:6]]()
            else:
                items[Player.inventory[itemChoice-1]]() 
            
            input("\nPress any key to continue..")
