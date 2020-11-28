# Main Game File for Gemhunter 2.
from npc import *

# Intro to Game
Introduction()


#~/ Main Loop \~#
while 1:
    InfoMessages()

    # Travel options
    roomIndex = player.room.name
    if rooms[roomIndex].up != None: print("up: %s  "%color("Room %s"%rooms[roomIndex].up, TextColor.blue),end = '')
    if rooms[roomIndex].down != None: print("down: %s  "%color("Room %s"%rooms[roomIndex].down, TextColor.blue), end = '')
    if rooms[roomIndex].left != None:  print("left: %s  "%color("Room %s"%rooms[roomIndex].left, TextColor.blue), end = '')
    if rooms[roomIndex].right != None: print("right: %s  "%color("Room %s"%rooms[roomIndex].right, TextColor.blue), end = '')

    # Players next location
    time.sleep(.175) # put this here because there was a threading issue when spamming keystrokes.  better than a crash.
    flush_input()   # flush input so you can't queue moves
    travelTo = ValidInput("\n%s "%color("->", TextColor.lightpurple),["w","a","s","d","m","menu"])
    
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
                print("You can't travel in that direction.  Pick a valid direction.")
                travelTo = ValidInput("\n%s "%color("->", TextColor.lightpurple),["w","a","s","d"])

        if player.room.door and player.room.door[0] == room.name:
            ClearConsole()
            doorKeys = ', '.join(player.room.door[2])
            playsound(boopSound, block=False)
            TypeOut("There is a %s in your path.  It requires: %s.\nWould you like to open it? (y/n)"%(player.room.door[1], doorKeys))
            openDoorInp = ValidInput("-> ",["y","n"])

            if openDoorInp == "y":
                opened = openDoor(player.room.door[2], doorName=player.room.door[1])
                if opened:
                    player.room = room
                else:
                    ClearConsole()
                    TypeOut("The door remains locked.")
            else:
                ClearConsole()
                TypeOut("The door remains locked.")
            time.sleep(1)

        else: 
            player.room = room
            if player.room.item:
                ClearConsole()
                playsound(newItem,False)
                ColorPrint("You found a %s!"%player.room.item, TextColor.yellow)
                time.sleep(1)
                player.inventory.append(player.room.item)
                player.room.item = None


        if player.room.npc: # if there is an npc in the room
            ClearConsole()
            playsound(foundSound,block=False)
            TypeOut("You found.. ",0.06,newline=False)
            time.sleep(.1)
            ColorPrint(" %s!\n\n"%player.room.npc, TextColor.yellow)
            time.sleep(2)

            interact = ValidInput("Would you like to interact with %s? (y/n)\n-> "%player.room.npc, ["y","n"])

            if interact == "y":
                npc[player.room.npc](player)
                
            else:
                TypeOut("%s watches you leave."%player.room.npc)
                time.sleep(1.5) 


    # Menu
    else:
        ClearConsole()
        playsound(boopSound, block=False)
        print("\tMenu\n1. Search Room." # prints a menu of options
            "\n2. Open Inventory."
            "\n3. View Quests.\n"
        )
        menuOption = ValidInput("-> ",["1","2","3","4", ""])
        playsound(boopSound, block=False)


        # Search Room
        if menuOption == "1":
            LoadingBar() 
            ClearConsole()
            #Room Items.
            if player.room.item: # if there is a item in the room
                playsound(newItem,block=False)
                TypeOut("You found a..",0.06, newline=False); ColorPrint(" %s!\n\n"%player.room.item, TextColor.yellow)
                if player.room.item == "Exit Door": 
                    input("Press any key to continue...")
                    WinGame() # Player won the game by finding the exit door
                else:
                    player.inventory.append(player.room.item)
                    player.room.item = None
                    time.sleep(2)

            elif not player.room.item and not random.randint(0,5):
                coinsAmount = random.randint(2,7)
                TypeOut("You found %g coins!"%coinsAmount)
                player.coins += coinsAmount

            else:  # if there is not an item
                TypeOut("There aren't any items in this room..")
                time.sleep(1.5)


        # Inspect inventory items.
        elif menuOption == "2":
            ClearConsole()
            ColorPrint("\nINVENTORY:", TextColor.blue)
            for index,name in enumerate(player.inventory):
                print("%g. %s"%(index+1, str(name)))

            TypeOut("\nWhich item do you want to inspect?\n",newline=False)
            flush_input()
            while True: # gets index input of the items
                try:
                    itemChoice = input("-> ")
                    if itemChoice == "": break
                    itemChoice = int(itemChoice)
                    player.inventory[itemChoice-1]
                    break
                except: pass

            if itemChoice == "": 
                pass

            else:
                if player.inventory[itemChoice-1] not in items:
                    items.update({player.inventory[itemChoice-1] : "An item."})

                if "Tunnel" in player.inventory[itemChoice-1]: # special case for tunnel bc the tunnel pass will rarely be the same across players games
                    ClearConsole()
                    items["Tunnel"]()

                elif "Gem" in player.inventory[itemChoice-1]:
                    ClearConsole()
                    items["Gem"]

                else:
                    ClearConsole()
                    items[player.inventory[itemChoice-1]]() if type(items[player.inventory[itemChoice-1]]) != str else TypeOut(items[player.inventory[itemChoice-1]])
                
                input("\nPress any key to continue..")
        

        # View Quests.
        elif menuOption == "3":
            ClearConsole()
            for index,name in enumerate(player.quests):
                print("%g. %s"%(index+1, str(name)))
            input("\n\nPress any key to continue..")
        

        # Developer Thread Info.
        elif menuOption == "4":
            ClearConsole()
            print("\t Debug Menu")
            print("ACTIVE THREAD COUNT: %g"%threading.active_count())
            input()

        else: pass
        