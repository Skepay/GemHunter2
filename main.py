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
Player.room = rooms[0].name
#Continue = Introduction()

Continue = "1" #TODO: Delete this line when out of development

# resume game
if Continue == "1":
    # open the map picture
    Image.open("Map.jpeg").show()

    while 1:
        TypeOut("You are currently in %s."%Player.room, 0.025)
        TypeOut("\nINVENTORY:\n%s"%', '.join(Player.inventory))
        input()
        
   



# start a new game
else:
    pass
    #TODO: make a way to play from save file lol

