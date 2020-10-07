import pickle
from src import *

# Main Game File for gemhunter
#TODO: puzzles, more mpcs, more content, search room func, with search room loading bar (15 second).  Save file, NPC's that can grant keys,use colors

#~/ Rooms \~#
roomFile = open('bin.dat','rb')
roomFile.seek(0)

class Room: # stores attributes of each room
        name = None
        item = None
        up = None
        down = None
        left = None
        right = None
        NPC = None
        
rooms = pickle.load(roomFile)


# Intro to Game
Introduction()

# Sets the player to start in the start room
Player.room = rooms[0]

# open the map picture
Image.open("Map.jpeg").show()


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
    travelTo = ValidInput("->","u","d","l","r","m","menu")

    # Travel.
    if "m" not in travelTo:
        keystrokes = {
                'u' : rooms[roomIndex].up,
                'd' : rooms[roomIndex].down,
                'l' : rooms[roomIndex].left,
                'r' : rooms[roomIndex].right
            }
        for i in rooms:
            if i.name == "Room %s"%keystrokes[travelTo]:
                Player.room = i


    # Menu
    else: 
        ClearConsole()
        print("Menu:\n1. Search Room." # prints a menu of options
            "\n2. Open Inventory."
            "\n3. Exit/Save Game.\n"
        )
        menuOption = input("->")
        

        # Search Room
        if menuOption == "1": # search room
            # credit JayPay loading bar
            ClearConsole()
            
            LoadingBar()

            ClearConsole()

            if Player.room.item: # if there is a item in the room
                TypeOut("You found..",0.06, newline=False); ColorPrint(" %s!"%Player.room.item, TextColor.yellow)
                
                Player.inventory.append(Player.room.item)

                time.sleep(2)

            else:  # if there is not an item
                TypeOut("There aren't any items in this room..")
                time.sleep(2)

            ClearConsole()

            if Player.room.NPC: # if there is an npc in the room
                TypeOut("You found..",0.06,newline=False); ColorPrint(" %s!"%Player.room.NPC, TextColor.yellow)
                time.sleep(2)

                interact = ValidInput("Would you like to interact with %s? (y/n)\n->"%Player.room.NPC, "y","n") 

                if interact == "y":
                    if Player.room.NPC == "PewDiePie": # if the npc is pewdiepie
                        PewDiePie()
                    #elif ..
                
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

            TypeOut("Which item do you want to inspect?")


            digit_list = ["0","1","2","3","4","5","6","7","8","9"]
            while True: # gets index input of the items
                itemChoice = input("->")
                if itemChoice not in digit_list:
                    itemChoice = input("->")

                elif int(itemChoice) in range(1,len(Player.inventory)+1) and itemChoice in digit_list:
                    itemChoice = int(itemChoice)
                    break
            inspectItem = items[Player.inventory[itemChoice-1]] # passes item in dictionary

            if inspectItem == "Chair": #for some reason, calling the function in a dictionary throws off the main loop.
                teleportRoom = Chair() # uses the chair

                for room in rooms: # teleports the player to his desired location
                    if room.name == "Room %s"%teleportRoom:
                        Player.room = room
                        Player.inventory.remove("PewDiePie 100M Edition Clutch Chair")
                        TypeOut("You have arrived!\n")
                        break
            
            else: # if the item isnt the chair
                TypeOut(inspectItem)
                    
            input("\nPress any key to continue..") 


        if menuOption == "3": # save game
            with open("save.py","w") as saveFile:
                saveFile.write("%s\n"%str(Player.name))
                saveFile.write("%s\n"%str(Player.inventory))
            input("Saved your progress.")
            exit(1)
        