import os, time, sys, subprocess, random
from PIL import Image
from color_source import ColorsFG, color, TextColor


#~/ Functions \~#
def ValidInput(string, param1, param2):
    inp = input(string)
    while 1:
        if inp == param1 or inp == param2:
            return inp
        inp = input(string)

# Get windows username of player.
def GetName():
    return os.getlogin()


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


#OG welcome message for gem hunter.
def Introduction():
    TypeOut('Welcome %s, to the text based adventure game...'%Player.name)
    time.sleep(0.5)
    TypeOut('G E M    H U N T E R',0.06)
    input('')

    ClearConsole()
    TypeOut("Would you like to:\n1. Continue\n2. New Game") # input options
    ClearConsole()     # clear the console
    continueGame = ValidInput("Would you like to:\n1. Continue\n2. New Game\n\n", "1", "2") # validate input
    return continueGame


#~/ Player \~#
class Player:
    name = GetName()
    inventory = ['surgical mask','gfuel']
    room = 0
