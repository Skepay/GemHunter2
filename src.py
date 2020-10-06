import os, time, sys, subprocess, random
from color_source import ColorsFG, color, TextColor

# Make sure PIL is installed
try:
    from PIL import Image
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'pillow'])
    print("Installed Pillow.")
    exit(1)
finally:
    from PIL import Image


#~/ Functions \~#
def ValidInput(string, param1, param2, param3 = None, param4 = None, param5 = None, param6 = None):
    validInputs = [param1,param2,param3,param4,param5,param6]
    inp = str(input(string))
    
    while 1:
        if inp in validInputs:
            return inp
        inp = str(input(string))


# Get windows username of player.
def GetName():
    return os.getlogin()


def LoadingBar():
    # credit JayPay
    dots = 0; bar = 0; loops = 0
    nextl = random.randint(0,10)

    while bar != 100:
        loops += 1
        loading = '\n\n\nSearching Room.'
        for i in range(loops % 4):
            loading += '.'
        print(loading)

        if loops == nextl:
            bar += 1
            nextl = random.randint(1,3)
            loops = 0

        barstring = '['
        for i in range(bar):
            if i % 5 == 0:
                barstring += '#'
        while len(barstring) != 21:
            barstring += '-'
        barstring += '] %g%%'%bar
        print(barstring)

        time.sleep(random.uniform(0.1,0.2))
        ClearConsole()


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
    TypeOut('Welcome %s, to the text based adventure game...'%Player.name)
    time.sleep(0.5)

    TypeOut('G E M    H U N T E R',0.06)
    time.sleep(1)
    print("Credit: Isaiah Harville, Joshua Payne.")
    time.sleep(1)
    return input("Press any key to continue. Or type help for a list of keybinds.\n")


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

#~/ Player \~#
class Player:
    name = GetName()
    inventory = ['surgical mask','gfuel']
    room = 0
