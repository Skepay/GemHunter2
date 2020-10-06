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


#~/ Main Loop \~#

# beginning of game
    #init player
        #begin introduction
Player.room = rooms[0]
#Continue = Introduction()

Continue = "1" #TODO: Delete this line when out of development

# resume game
if Continue == "1":
    # open the map picture
    #Image.open("Map.jpeg").show()
    #TODO: save inventory to a file and read it from there

    while 1:
        ClearConsole()
        # informational messages
        TypeOut("You are currently in ", 0.015,newline=False); ColorPrint(Player.room.name,TextColor.blue)
        ColorPrint("\nINVENTORY:", TextColor.blue)
        TypeOut("%s"%', '.join(Player.inventory),0.015)

        # location messages
        print("Where would you like to travel to?",end =''); ColorPrint(" (u/d/l/r/m)",TextColor.lightpurple)

        roomIndex = rooms.index(Player.room)    #ignore the stupidly long and ugly print statement below
        print("up:",color("Room %s"%rooms[roomIndex].up, TextColor.blue),"down:",color("Room %s"%rooms[roomIndex].down, TextColor.blue),"left:",color("Room %s"%rooms[roomIndex].left, TextColor.blue),"right:",color("Room %s"%rooms[roomIndex].right, TextColor.blue))
        
        # next location
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
                if Player.room.NPC != None:
                    TypeOut("You found..",0.06,newline=False)
                    ColorPrint(" %s!"%Player.room.NPC, TextColor.yellow)
                time.sleep(5)
            

            if menuOption == "2":
                ColorPrint("\nINVENTORY:", TextColor.blue)
                TypeOut("%s"%', '.join(Player.inventory),0.015)


        else:
            keystrokes = {
                'u' : rooms[roomIndex].up,
                'd' : rooms[roomIndex].down,
                'l' : rooms[roomIndex].left,
                'r' : rooms[roomIndex].right
            }
            for i in rooms:
                if i.name == "Room %s"%keystrokes[travelTo]:
                    Player.room = i


                







# start a new game
else:
    pass
    #TODO: make a way to play from save file lol

