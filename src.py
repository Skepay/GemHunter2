# Source File for Gem Hunter containing all background work.
import os
import random
import subprocess
import sys
import time

from color_source import ColorsFG, TextColor, color
from Map import rooms

try:
    from playsound import playsound
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'playsound'])
finally:
    from playsound import playsound

#~/ Sounds \~#
# set second arguement to be False, so it will run async
soundPath = "%sSounds"%os.path.abspath(__file__)[0:-6]
spitSound = "%s\spit.mp3"%soundPath
boopSound = "%s\Sboop.mp3"%soundPath
teleportSound = "%s\teleportSound.mp3"%soundPath
introSong = "%s\intro_song.mp3"%soundPath
winSound = "%s\win.mp3"%soundPath
newItem = "%s\_newItem.mp3"%soundPath
foundSound = "%s\_found.mp3"%soundPath
error = "%s\error.mp3"%soundPath
phoneRing = "%s\walterWhitesRingtone.mp3"%soundPath



#~/ Functions \~#
# Valid Input function
def ValidInput(string, params):
    inp = str(input(string))
    while 1:
        playsound(boopSound, block=False) #TODO: remove this if there is weird stuff
        if inp in params:
            return inp
        inp = str(input(string))


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


def Story():
    ClearConsole()
    with open("files/story.txt", "r") as sf:
        sdata = sf.read().splitlines()
    
    for i in sdata:
        if i != "NEW":
            TypeOut(i)
            time.sleep(1)
        else:
            time.sleep(2)
            input("\nPress any key to continue..")
            ClearConsole()
    print()
    time.sleep(2)
    ColorPrint("TEST SUBJECT: ", TextColor.red, newLine=False)
    time.sleep(1.75)
    ColorPrint("Dr. %s"%player.name, TextColor.red)
    time.sleep(2)

    input("Press any key to continue to the game..")


# OG welcome message for gem hunter.
def Introduction():
    playsound(introSong, block=False)
    time.sleep(.5)
    ClearConsole()
    TypeOut('Welcome %s, to the text based adventure game...'%player.name)
    time.sleep(0.60)
    TypeOut('G E M    H U N T E R',0.075)
    time.sleep(2.15)
    ClearConsole()
    ColorPrint("Developed By: ", TextColor.green); TypeOut("Isaiah Harville, Joshua Payne, and Colin O'Kain.",0.06)
    time.sleep(5)
    InfoInp = input("Press enter to continue. Or type help for a list of keybinds.\n")
    Instructions() if InfoInp else Story()


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
    ColorPrint("LOCATION", TextColor.blue)
    playsound(boopSound, block=False)
    TypeOut("You are currently in ", 0.010,newline=False); ColorPrint("Room %g"%player.room.name,TextColor.blue) # types out the name of color in blue
    ColorPrint("\nINVENTORY", TextColor.blue)
    TypeOut(', '.join(player.inventory),0.010)
    ColorPrint("HEALTH: %g  COINS: %g\n"%(player.hp, player.coins), TextColor.blue)
    print("Where would you like to travel to?",end =''); ColorPrint(" (w/a/s/d/m)",TextColor.lightpurple)



#~/ Doors \~#
def openDoor(keys, doorName):
    missingKeys = []
    for key in keys:
        if key not in player.inventory:
            missingKeys.append(key)

    if len(missingKeys): # if player does not have keys
        ClearConsole()
        TypeOut("You do not have: %s."%', '.join(missingKeys))
        time.sleep(1)
        return False

    else:  # if the player has the keys
        ClearConsole()
        TypeOut("The %s opened!"%doorName, 0.06)
        player.room.door = None
        for key in keys:
            player.inventory.remove(key)
        time.sleep(1)
        return True



#~/ Item Functions\~#
# Informational message about gfuel.
def Gfuel():
    ClearConsole()
    TypeOut("A tasty beverage.")


# Function for the PewDiePie chair item.
def Chair():
    ClearConsole()

    useChair = ValidInput('This chair can teleport you to any room.. in STYLE.\nWould you like to use it?\n(y/n)\n\n-> ', ["y", "n"])
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
                player.room = room
                player.inventory.remove("PewDiePie 100M Edition Clutch Chair")
                playsound(teleportSound, block=False)
                TypeOut("You have arrived in Room %s!\n"%player.room.name,0.06)
                time.sleep(1)
                break
    else:
        ClearConsole()
        TypeOut("The chair will be waiting for you.")


# Function for the tunnel
def Tunnel():
    ClearConsole()

    # find room where elon spawns
    for i in player.inventory:
        if "Tunnel" in i:
            Card = player.inventory.index(i)
            break

    # if there is already a made tunnel
    if "CONNECTED" in player.inventory[Card]:
        ElonRoom = int(player.inventory[Card][13:player.inventory[Card].index("(")-1])  
        endRoom = int(player.inventory[Card][player.inventory[Card].index(":")+2:-1])

    # if there isnt
    else:
        TypeOut("MR. TUNNEL BUILDER: Please keep in mind, after you make a tunnel, the tunnel is permanent and can not be changed.")
        time.sleep(1)
        while True:
            ClearConsole()
            try:
                endRoom = int(input("What is the number of the room you want to tunnel to?\n-> "))
                if endRoom in range(0,len(rooms)):
                    break
            except ValueError:
                pass
        ElonRoom = int(player.inventory[Card][13:])  
        player.inventory.append("%s (CONNECTED TO: %s)"%(player.inventory[Card], endRoom))
        player.inventory.remove(player.inventory[Card])
    

    # if player is in the start tunnel room
    if player.room.name != ElonRoom:
        ClearConsole()
        TypeOut("You are not in the tunnel's starting room so you can not travel in this tunnel.")
        return None

    ClearConsole()
    TypeOut("The start of the tunnel is located in Room %s.  The tunnel leads to Room %s.\n"%(ElonRoom, endRoom), newline=False)
    useTunnel = ValidInput("Use Tunnel? (y/n)\n\n-> ", ["y", "n"])
    if useTunnel == "y":
        ClearConsole()
        TypeOut("ZOOOOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.", .03)
        player.room = rooms[endRoom]
        TypeOut("You have arrived in Room %s!\n"%player.room.name)
        time.sleep(1)
    else:
        ClearConsole()
        TypeOut("*tunnel noises*")
        time.sleep(1)


# Function for health potions.
def HealthPotion():
    try:
        potionType = player.inventory.index('Large Health Potion')
        healAmount = 10
    except ValueError:
        potionType = player.inventory.index('Small Health Potion')
        healAmount = 5
    
    player.hp += healAmount
    if player.hp > 20:
        player.hp = 20

    TypeOut('You used a %s and restored your hp to %g!'%(player.inventory[potionType], player.hp))
    player.inventory.remove(player.inventory[potionType])


# Function for Cesium.
def Cesium():
    ClearConsole()
    TypeOut("What would you like to mix this with?\n", newline=False)
    for index, i in enumerate(player.inventory):
        print("%g. %s"%(index+1, i))
    print()
    while True: # gets index input of the items
        try:
            itemChoice = int(input("-> "))
            if int(itemChoice) in range(0,len(player.inventory)-1) or itemChoice == len(player.inventory):
                break
        except:
            pass

    if player.inventory[itemChoice].lower() == "water":
        ClearConsole()
        player.inventory.remove(player.inventory[itemChoice])
        player.inventory.remove('Cesium')
        TypeOut("You made a Cesium bomb by mixing Cesium-137 with H2O!\n", newline=False)
        if "Hazmat Suit" in player.inventory:
            TypeOut("Thanks to your Hazmat Suit, you aren't affected by the radiation.")
        else:
            TypeOut("The radiation is toxic to your health and you take significant damage.")
            player.hp = player.hp/2

        if player.room.door:
            player.room.door = None
            TypeOut("Somehow.. you managed to blow up a door!")
            time.sleep(1)
        time.sleep(1)
        return
    else:
        TypeOut("Well.. that won't do much..")
        time.sleep(1)
        return
            
        

# Dictionary for the items
items = {
    'GFUEL' : Gfuel,
    'PewDiePie 100M Edition Clutch Chair' : Chair,
    'Tunnel' : Tunnel,
    'Maya\'s Eyepatch' : "Return this item to Maya!",
    'Large Health Potion' : HealthPotion,
    'Small Health Potion' : HealthPotion,
    'Cesium' : Cesium,
    'Hazmat Suit' : "Protects you from radiation.\nIf you somehow managed to find any. . .",
    'Blue Ice Gfuel' : "Deliver this item to Walter White.",
    "Walter's 24\" Pizza" : "A pizza Walter White gave to you because his wife is a whore."
    }



#~/ Player \~#
class Player:
    def __init__(self):
        self.hp = 20
        self.name = GetName()
        self.inventory = ["GFUEL"]
        self.room = rooms[0]
        self.coins = 0
        self.quests = []

    def Punch(self, enemy):
        item = enemy.Damage(random.randint(2,5))
        if(item):
            self.inventory.append(item)

    def Kick(self, enemy):
        item = enemy.Damage(random.randint(0,7))
        if(item):
            self.inventory.append(item)

    def GetHealth(self):
        return self.hp

    def HasSpecialItems(self):
        return False


player = Player()