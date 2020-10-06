import pickle
from src import *

#TODO: puzzles, more mpcs, more content, search room func, with search room loading bar (15 second).  Save file, NPC's that can grant keys,use colors

#~/ Rooms \~#
roomFile = open('bin.dat','rb')
roomFile.seek(0)

class Room:
        name = None
        item = None
        up = None
        down = None
        left = None
        right = None
        NPC = None
        
rooms = pickle.load(roomFile)


# Intro to Game
start = Introduction()
if start == "help":
    Instructions()

# Sets the player to start in the start room
Player.room = rooms[0]

# open the map picture
#Image.open("Map.jpeg").show()


#~/ Main Loop \~#
while 1:
    ClearConsole()

    # Informational messages
    TypeOut("You are currently in ", 0.010,newline=False); ColorPrint(Player.room.name,TextColor.blue)
    time.sleep(.5)
    
    ColorPrint("\nINVENTORY:", TextColor.blue)
    print("%s\n"%', '.join(Player.inventory))

    # location messages
    print("Where would you like to travel to?",end =''); ColorPrint(" (u/d/l/r/m)",TextColor.lightpurple)

    # Travel options
    roomIndex = rooms.index(Player.room)    #ignore the stupidly long and ugly print statement below
    print("up:",color("Room %s,"%rooms[roomIndex].up, TextColor.blue),"down:",color("Room %s,"%rooms[roomIndex].down, TextColor.blue),"left:",color("Room %s,"%rooms[roomIndex].left, TextColor.blue),"right:",color("Room %s,"%rooms[roomIndex].right, TextColor.blue))
      
    # Players next location
    travelTo = ValidInput("->","u","d","l","r","m","menu")

    if travelTo == "m" or travelTo == "menu": # open menu
        ClearConsole()
        print("Menu:\n1. Search Room."
            "\n2. Open Inventory."
            "\n3. Exit/Save Game.\n"
        )
        menuOption = ValidInput("->", "1","2","3")
        

        # Search Room
        if menuOption == "1": # search room
            # credit JayPay loading bar
            ClearConsole()
            
            LoadingBar()

            if Player.room.item != None:
                TypeOut("You found..",0.06, newline=False)
                ColorPrint(" %s!"%Player.room.item, TextColor.yellow)
            else:
                TypeOut("There aren't any items in this room..")

            if Player.room.NPC != None:
                TypeOut("You found..",0.06,newline=False)
                ColorPrint(" %s!"%Player.room.NPC, TextColor.yellow)
            else:
                TypeOut("There aren't any NPCs in this room..")

            time.sleep(5)
        

        if menuOption == "2": # inspecting items in inventory
            ClearConsole()

            ColorPrint("\nINVENTORY:", TextColor.blue)
            for index,name in enumerate(Player.inventory):
                print("%g. %s"%(index+1, str(name)))

            TypeOut("Which item do you want to inspect?")

            digit_list = ["0","1","2","3","4","5","6","7","8","9"]
            while True:
                itemChoice = input("->")
                if itemChoice not in digit_list:
                    itemChoice = input("->")
                elif int(itemChoice) in range(1,len(Player.inventory)+1) and itemChoice in digit_list:
                    itemChoice = int(itemChoice)
                    break
            
            items = {
                'surgical mask' : "A mask to protect you from coronavirus.",
                'gfuel' : "Gotta stay awake when you're solving those puzzles."
            }

            TypeOut(items[Player.inventory[itemChoice-1]])
            input("\nPress any key to continue..")


        if menuOption == "3": # save game
            with open("save.py","w") as saveFile:
                saveFile.write("%s\n"%str(Player.name))
                saveFile.write("%s\n"%str(Player.inventory))
            input("Saved your progress.")
            exit(1)


    else: # traveling rooms
        keystrokes = {
            'u' : rooms[roomIndex].up,
            'd' : rooms[roomIndex].down,
            'l' : rooms[roomIndex].left,
            'r' : rooms[roomIndex].right
        }
        for i in rooms:
            if i.name == "Room %s"%keystrokes[travelTo]:
                Player.room = i