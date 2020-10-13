# Main Game File for gemhunter
from npc import *

# Intro to Game
# TODO: Uncomment this for production -> Introduction()

#~/ Main Loop \~#
while 1:
    InfoMessages()

    # Travel options
    roomIndex = rooms.index(Player.room)    # this stupidly long and ugly print statement below, will type out move locations in blue
    print("up:",color("Room %s,"%rooms[roomIndex].up, TextColor.blue),"down:",color("Room %s,"%rooms[roomIndex].down, TextColor.blue),"left:",color("Room %s,"%rooms[roomIndex].left, TextColor.blue),"right:",color("Room %s,"%rooms[roomIndex].right, TextColor.blue))
    
    # Players next location
    travelTo = ValidInput("-> ",["w","a","s","d","m","menu"])
    
    # Travel.
    if "m" not in travelTo:
        keystrokes = {
                'w' : rooms[roomIndex].up,
                's' : rooms[roomIndex].down,
                'a' : rooms[roomIndex].left,
                'd' : rooms[roomIndex].right
            }

        while 1:
            try:
                room = rooms[keystrokes[travelTo]]
                break
            except (NameError, TypeError):
                travelTo = ValidInput("-> ",["w","a","s","d"])
        
        
        if Player.room.door and Player.room.door[0] == room.name:
            ClearConsole()

            doorKeys = ', '.join(Player.room.door[2])

            TypeOut("There is a %s in your path.  It requires: %s.\nWould you like to open it? (y/n)"%(Player.room.door[1], doorKeys))
            openDoorInp = ValidInput("-> ",["y","n"])

            if openDoorInp == "y":
                opened = openDoor(Player.room.door[2], doorName=Player.room.door[1])
                if opened:
                    Player.room = room
                else:
                    ClearConsole()
                    TypeOut("The door remains locked.")
            else:
                ClearConsole()
                TypeOut("The door remains locked.")
            time.sleep(1)

        else: # if there is not a door
            Player.room = room


        if Player.room.npc: # if there is an npc in the room
            ClearConsole()
            TypeOut("You found.. ",0.06,newline=False); ColorPrint(" %s!\n\n"%Player.room.npc, TextColor.yellow)
            time.sleep(2)

            interact = ValidInput("Would you like to interact with %s? (y/n)\n-> "%Player.room.npc, ["y","n"])

            if interact == "y":
                npc[Player.room.npc]()

            else:
                TypeOut("%s sadly sits alone."%Player.room.npc)
                time.sleep(1.5) 


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
                Player.room.item = None
                time.sleep(2)

            else:  # if there is not an item
                TypeOut("There aren't any items in this room..")
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
            
            if Player.inventory[itemChoice-1] not in items:
                items.update({Player.inventory[itemChoice-1] : "An item."})

            if "Tunnel" in Player.inventory[itemChoice-1]: # special case for tunnel bc the tunnel pass will rarely be the same across players games
                ClearConsole()
                items["Tunnel"]()
            else:

                ClearConsole()
                items[Player.inventory[itemChoice-1]]() if type(items[Player.inventory[itemChoice-1]]) != str else TypeOut(items[Player.inventory[itemChoice-1]])
            
            input("\nPress any key to continue..")


