# Source File for Gem Hunter containing all background work.
import os, time, sys, subprocess, random
from color_source import ColorsFG, color, TextColor

# Define rooms to get rid of syntax errors.
rooms = [0]

# Valid Input function
def ValidInput(string, param1, param2, param3 = None, param4 = None, param5 = None, param6 = None):
    validInputs = [param1,param2,param3,param4,param5,param6]
    inp = str(input(string))

    while 1:
        if inp in validInputs:
            return inp
        inp = str(input(string))


#~/ Doors \~#
def openDoor(keys):
    missingKeys = []
    if type(keys) == list:
        for key in keys:
            if key not in Player.inventory:
                missingKeys.append(key)
    else:
        if keys not in Player.inventory:
            missingKeys.append(keys)

    if len(missingKeys):
        TypeOut("You do not have: %s."%', '.join(missingKeys))
        time.sleep(1)

        return False

    else:
        TypeOut("The door opened!", 0.06)

        if type(keys) == list:
            for key in keys:
                Player.inventory.remove(key)
        else:
            Player.inventory.remove(keys)

        time.sleep(1)

        return True

key = {
    'Red Door' : 'Red Key',
    'Orange Door' : 'Orange Key',
    'Yellow Door' : 'Yellow Key',
    'Green Door' : 'Green Key',
    'Blue Door' : 'Blue Key',
    'Indigo Door' : 'Indigo Key',
    'Violet Door' : 'Violet Key',
    'Gemstone Door' : ['Red Key', 'Orange Key', 'Yellow Key', 'Green Key', 'Blue Key', 'Indigo Key', 'Violet Key']
}

#~/ Item Functions\~#
# Informational messagfe about gfuel.
def Gfuel():
    ClearConsole()
    TypeOut("A tasty beverage.")


# Function for the PewDiePie chair item.
def Chair(rooms):
    ClearConsole()

    useChair = ValidInput('This chair can teleport you to any room.. in STYLE.\nWould you like to use it?\n(y/n)\n\n-> ', "y", "n")
    if useChair == "y":
        ClearConsole()

        # verify the input of the room 
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

        # teleports the player to his desired location
        for room in rooms:
            if room.name == "Room %s"%teleportLocation:
                Player.room = room
                Player.inventory.remove("PewDiePie 100M Edition Clutch Chair")
                TypeOut("You have arrived!\n",0.06)
                break
    else:
        ClearConsole()
        TypeOut("The chair will be waiting for you.")


# Dictionary for the items
items = {
    'GFUEL' : Gfuel,
    'PewDiePie 100M Edition Clutch Chair' : Chair
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
        time.sleep(random.uniform(0.005,.100))
        

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
    time.sleep(0.5)

    TypeOut('G E M    H U N T E R',0.06)
    time.sleep(1)

    print("Credit: Isaiah Harville, Joshua Payne, Colin O'Kain, Matthew Payne.")
    time.sleep(1)

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
    room = 0

    def punch(enemy):
        item = enemy.Damage(random.randint(0,4))
        if(item):
            inventory.append(item)