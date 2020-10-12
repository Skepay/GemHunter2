# Source File for Gem Hunter containing all background work.
import os
import random
import subprocess
import sys
import time

from color_source import ColorsFG, TextColor, color
from Map import rooms


# Valid Input function
def ValidInput(string, []):
    validInputs = [param1,param2,param3,param4,param5,param6]
    inp = str(input(string))
    while 1:
        if inp in validInputs:
            return inp
        inp = str(input(string))

<<<<<<< HEAD
=======
# Get windows username of player.
def GetName():
    return os.getlogin()

# Loading bar animation.
def LoadingBar():
    progress = 0
    while progress <= 100:
        ClearConsole()
        progressBars = progress // 5
        print('Searching Room%s'%('.' * (progress % 4)))
        print('[%s%s] %g%%'%('#' * progressBars, '-' * (20 - progressBars), progress))
        progress += 1
        time.sleep(random.uniform(0.0075,.100))
        
# Clear the console
def ClearConsole(newline = False):
    os.system('cls')
    if newline:
        print()

# Type Out messages.
def TypeOut(string, pause = 0.045, newline = True):
    for letter in string:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(pause)

    if newline:
        print("\n")

# Print Colored messages.
def ColorPrint(string, inputColor = TextColor.white):
    print(color(string, inputColor))

# OG welcome message for gem hunter.
def Introduction():
    ClearConsole()
    TypeOut('Welcome %s, to the text based adventure game...'%Player.name)
    time.sleep(0.75)
    TypeOut('G E M    H U N T E R',0.075)
    time.sleep(3)
    ClearConsole()
    ColorPrint("Developed By: ", TextColor.green); TypeOut("Isaiah Harville, Joshua Payne, and Colin O'Kain.",0.06)
    time.sleep(5)
    InfoInp = input("Press enter to continue. Or type help for a list of keybinds.\n")
    Instructions() if InfoInp else print()

# List of keybinds for the game.
def Instructions():
    print("""
        "W" -> Moves up\n
        "S" -> Moves down\n
        "A" -> Moves left\n
        "D" -> Moves right\n
        "M" or "menu" -> Opens the menu.
        """)
    input("\n\nPress any key to continue.")

# Prints informational messages.
def InfoMessages():
    ClearConsole()
    ColorPrint("LOCATION:", TextColor.blue)
    TypeOut("You are currently in ", 0.010,newline=False); ColorPrint("Room %s"%str(Player.room.name),TextColor.blue) # types out the name of color in blue
    ColorPrint("\nINVENTORY:", TextColor.blue)
    TypeOut(', '.join(Player.inventory),0.010)
    print("Where would you like to travel to?",end =''); ColorPrint(" (w/a/s/d/m)",TextColor.lightpurple)

>>>>>>> 5f9242cac1a0e0245022c641c58be4a7dbcd0041

#~/ Doors \~#
def openDoor(keys, doorName): 
    missingKeys = []
    for key in keys:
        if key not in Player.inventory:
            missingKeys.append(key)

    if len(missingKeys): # if player does not have keys
        ClearConsole()
        TypeOut("You do not have: %s."%', '.join(missingKeys))
        time.sleep(1)
        return False

    else:  # if the player has the keys
        ClearConsole()
        TypeOut("The %s Door opened!"%doorName, 0.06)
        for key in keys:
            Player.inventory.remove(key)
        time.sleep(1)
        return True

key = {
    'Red Door' : ['Red Key'],
    'Orange Door' : ['Orange Key'],
    'Yellow Door' : ['Yellow Key'],
    'Green Door' : ['Green Key'],
    'Blue Door' : ['Blue Key'],
    'Indigo Door' : ['Indigo Key'],
    'Violet Door' : ['Violet Key'],
    'Gemstone Door' : ['Red Key', 'Orange Key', 'Yellow Key', 'Green Key', 'Blue Key', 'Indigo Key', 'Violet Key']
}


#~/ Item Functions\~#
# Informational message about gfuel.
def Gfuel():
    ClearConsole()
    TypeOut("A tasty beverage.")


# Function for the PewDiePie chair item.
def Chair():
    ClearConsole()

    useChair = ValidInput('This chair can teleport you to any room.. in STYLE.\nWould you like to use it?\n(y/n)\n\n-> ', "y", "n")
    if useChair == "y":
        ClearConsole()

        # verify the input of the room 
        while True:
            ClearConsole()
            try:
                teleportLocation = int(input("What is the number of the room you want to travel to?\n-> "))
                if teleportLocation in range(0,len(rooms)):
                    break
            except:
                pass

        # teleports the player to his desired location
        for room in rooms:
            if room.name == teleportLocation:
                Player.room = room
                Player.inventory.remove("PewDiePie 100M Edition Clutch Chair")
                TypeOut("You have arrived in Room %s!\n"%Player.room.name,0.06)
                break
    else:
        ClearConsole()
        TypeOut("The chair will be waiting for you.")


# function for the tunnel
def Tunnel():
    ClearConsole()

    # find room where elon spawns
    for i in Player.inventory:
        if "Tunnel" in i:
            CardNum = Player.inventory.index(i)
            break

    ElonRoom = int(Player.inventory[CardNum][13:])
    for room in rooms:
        if room.name == ElonRoom:
            startRoom = room

    # if there is already a made tunnel
    if len(Player.inventory[CardNum]) > 16:
        endRoom = []
        for i in Player.inventory[CardNum][17:]:
            try:
                int(i)
                endRoom.append(int(i))
            except ValueError:
                pass
        endRoom = int(''.join(map(str, endRoom)))

    # if there isnt
    else:
        TypeOut("MR. TUNNEL BUILDER: Please keep in mind, after you make a tunnel, that is permanent and can not be changed.")
        while True:
            ClearConsole()
            try:
                endRoom = int(input("What is the number of the room you want to tunnel to?\n-> "))
                if endRoom in range(0,len(rooms)-1):
                    break
            except ValueError:
                pass
        Player.inventory.append("%s (CONNTECTED TO: %s"%(Player.inventory[CardNum], endRoom))
        Player.inventory.remove(Player.inventory[CardNum])

    ClearConsole()
    TypeOut("The start of the tunnel is located in Room %s.  The tunnel leads to Room %s."%(startRoom, endRoom), newline=False)
    ValidInput("Use Tunnel? (y/n)\n\n-> ", "y", "n")
    if ValidInput == "y":
        ClearConsole()
        TypeOut("ZOOOOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.",.03)
        for room in rooms:
            if room.name == endRoom:
                Player.room = room

        TypeOut("You have arrived in Room %s\n"%Player.room.name)
        time.sleep(1)
    else:
        TypeOut("*tunnel noises*")
        time.sleep(1)


# Dictionary for the items
items = {
    'GFUEL' : Gfuel,
    'PewDiePie 100M Edition Clutch Chair' : Chair,
    'Tunnel' : Tunnel,
}


#~/ Functions \~#

# Get windows username of player.
def GetName():
    return os.getlogin()


# Loading bar animation.
def LoadingBar():
    progress = 0
    while progress <= 100:
        ClearConsole()
        progressBars = progress // 5
        print('Searching Room%s'%('.' * (progress % 4)))
        print('[%s%s] %g%%'%('#' * progressBars, '-' * (20 - progressBars), progress))
        progress += 1
        time.sleep(random.uniform(0.0075,.100))
        

# Clear the console
def ClearConsole(newline = False):
    os.system('cls')
    if newline:
        print()


# Type Out messages.
def TypeOut(string, pause = 0.045, newline = True):
    for letter in string:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(pause)

    if newline:
        print("\n")


# Print Colored messages.
def ColorPrint(string, inputColor = TextColor.white, newLine = True):
    print(color(string, inputColor), end = '')
    if newLine:
        print('')


# OG welcome message for gem hunter.
def Introduction():
    ClearConsole()
    TypeOut('Welcome %s, to the text based adventure game...'%Player.name)
    time.sleep(0.75)
    TypeOut('G E M    H U N T E R',0.075)
    time.sleep(3)
    ClearConsole()
    ColorPrint("Developed By: ", TextColor.green); TypeOut("Isaiah Harville, Joshua Payne, and Colin O'Kain.",0.06)
    time.sleep(5)
    InfoInp = input("Press enter to continue. Or type help for a list of keybinds.\n")
    Instructions() if InfoInp else print()


# List of keybinds for the game.
def Instructions():
    print("""
        "U" -> Moves up\n
        "D" -> Moves down\n
        "L" -> Moves left\n
        "R" -> Moves right\n
        "M" or "menu" -> Opens the menu.
        """)
    input("\n\nPress any key to continue.")


# Prints informational messages.
def InfoMessages():
    ClearConsole()
    ColorPrint("LOCATION:", TextColor.blue)
    TypeOut("You are currently in ", 0.010,newline=False); ColorPrint(str(Player.room.name),TextColor.blue) # types out the name of color in blue
    ColorPrint("\nINVENTORY:", TextColor.blue)
    TypeOut("%s"%', '.join(Player.inventory),0.010)
    print("Where would you like to travel to?",end =''); ColorPrint(" (u/d/l/r/m)",TextColor.lightpurple)
    


#~/ Player \~#
class Player:
    name = GetName()
    health = 20
    inventory = ["GFUEL"]
    room = rooms[0]

    def punch(self, enemy):
        item = enemy.Damage(random.randint(0,4))
        if(item):
            inventory.append(item)

    def addToInventory(self, item):
        inventory.append(item)
        
