# Source File for Gem Hunter containing all background work.
import os
import random
import subprocess
import sys
import time
import threading

from color_source import ColorsFG, TextColor, color
from Map import rooms

# Install required libraries.
try: from playsound import playsound
except ImportError: subprocess.call([sys.executable, "-m", "pip", "install", 'playsound'])
finally: from playsound import playsound

try: from pyfiglet import Figlet
except ImportError: subprocess.call([sys.executable, "-m", "pip", "install", 'pyfiglet'])
finally: from pyfiglet import Figlet

try: import pyautogui
except ImportError: subprocess.call([sys.executable, "-m", "pip", "install", 'pyautogui'])
finally: import pyautogui



#~/ Sounds \~#
# set second arguement to be False, so it will run async
soundPath = r"%sSounds"%os.path.abspath(__file__)[0:-6]
spitSound = r"%s\spit.mp3"%soundPath
boopSound = r"%s\Sboop.mp3"%soundPath
teleportSound = r"%s\_teleportSound.mp3"%soundPath
introSong = r"%s\intro_song.mp3"%soundPath
winSound = r"%s\win.mp3"%soundPath
newItem = r"%s\_newItem.mp3"%soundPath
foundSound = r"%s\_found.mp3"%soundPath
error = r"%s\error.mp3"%soundPath
phoneRing = r"%s\walterWhitesRingtone.mp3"%soundPath



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
    if inputColor == "rainbow":
        textColors = [TextColor.red, TextColor.orange, TextColor.yellow, TextColor.green, TextColor.blue, TextColor.purple, TextColor.white]
        for i in string:
            print(color(i, random.choice(textColors)), end='')
        print()
    else:
        print(color(string, inputColor), end = '')
        if newLine:
            print()


# Print Title.
def TitlePrint():
    ft = Figlet(font="slant")
    ColorPrint(str(ft.renderText("GEM HUNTER")), inputColor=TextColor.green)


# Cringe Back story.
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
    time.sleep(2)
    ColorPrint("TEST SUBJECT: ", TextColor.red, newLine=False)
    time.sleep(1.75)
    ColorPrint("Dr. %s"%player.name, TextColor.red)
    time.sleep(2)

    input("Press any key to continue to the game..")


# OG welcome message for gem hunter.
def Introduction():
    playsound(introSong, block=False)
    time.sleep(.6)
    ClearConsole()
    TypeOut('Welcome %s, to the text based adventure game...'%player.name)
    time.sleep(0.60)
    TitlePrint()
    time.sleep(4.5)
    ClearConsole()
    ColorPrint("Developed By: ", TextColor.green); TypeOut("Isaiah Harville, Joshua Payne, and Colin O'Kain.",0.06)
    time.sleep(5)
    InfoInp = input("Press enter to continue. Or type help for a list of keybinds.\n")
    Instructions() if InfoInp else Story()


# List of keybinds for the game.
def Instructions():
    print("""
        "w" -> Moves up\n
        "s" -> Moves down\n
        "a" -> Moves left\n
        "d" -> Moves right\n
        "m" or "menu" -> Opens the menu.
        """)
    input("\n\nPress any key to continue.")


# Prints informational messages.
def InfoMessages():
    ClearConsole()
    ColorPrint("LOCATION", TextColor.blue)
    playsound(boopSound, block=False)
    TypeOut("You are currently in ", 0.010, newline=False); ColorPrint("Room %g"%player.room.name,TextColor.blue) # types out the name of color in blue
    ColorPrint("\nINVENTORY", TextColor.blue)
    print(', '.join(player.inventory),end="\n\n")
    print("%s: %g  %s: %g\n"%(color("HEALTH", TextColor.blue), player.hp, color("COINS",TextColor.blue), player.coins))
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



#~/ Doors \~#
def WinGame():
    st = Figlet(font="slant")
    ClearConsole()
    time.sleep(1)
    TypeOut("You approach the exit door and see the bright sun.")
    TypeOut("Without hesitation, you walk into the fresh outdoors.")
    time.sleep(4)
    playsound(winSound,block=False)
    time.sleep(1)
    ColorPrint(str(st.renderText("GAME OVER")), inputColor=TextColor.green)
    time.sleep(3)
    ClearConsole()
    TypeOut("Thank you for playing",newline=False)
    for i in "...":
        print(i,end='')
        time.sleep(.15)
    print("\n\n")
    time.sleep(1)
    ColorPrint(str(st.renderText("GEM HUNTER")), inputColor=TextColor.green)
    time.sleep(5)
    input("\nPress any key to continue..")
    ClearConsole()
    ColorPrint(str(st.renderText("SCORE")), inputColor=TextColor.blue)
    score = len(player.inventory) + player.hp + player.coins - player.deaths
    playsound(newItem,block=False)
    ColorPrint(str(st.renderText(str(score))), inputColor=TextColor.yellow)
    time.sleep(.5)
    pyautogui.screenshot().save(r"%s\GemHunter2Score.png"%os.path.abspath(__file__)[0:-6]) # take a screenshot of the player's score
    time.sleep(5)
    ClearConsole()
    time.sleep(.5)
    TypeOut("ISAIAH: Well this is the end, player.")
    time.sleep(1)
    TypeOut("ISAIAH: I'm not making another one of these so I hope you enjoyed it.")
    time.sleep(5)
    input("Press any key to exit..")
    exit()



#~/ Item Functions\~#
# Function for GFUEL.
def Gfuel():
    TypeOut("A tasty beverage.")
    time.sleep(1)
    TypeOut("Would you like to drink it? (y/n)")
    drink = ValidInput("\n-> ", ["y","n" ])
    if drink == "y":
        ClearConsole()
        player.inventory.remove("GFUEL")
        player.inventory.append("Empty GFUEL Shaker")
        player.hp += 1
        time.sleep(1)
        ColorPrint("20% MUSCLE INCREASE!!!", TextColor.yellow)

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
            except: pass


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
                rooms[endRoom]
                break
            except: pass

        ElonRoom = int(player.inventory[Card][13:])  
        player.inventory.append("%s (CONNECTED TO: %s)"%(player.inventory[Card], endRoom))
        player.inventory.remove(player.inventory[Card])
        #ElonRoom = int(player.inventory[Card][13:])  
    

    # if player is in the start tunnel room
    if player.room.name != ElonRoom:
        ClearConsole()
        TypeOut("You are not in the tunnel's starting room so you can not travel in this tunnel.")
        return

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
    if player.hp > 20: player.hp = 20

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
            player.inventory[itemChoice-1]
            break
        except: pass

    if player.inventory[itemChoice].lower() == "water":
        ClearConsole()
        player.inventory.remove(player.inventory[itemChoice])
        player.inventory.remove('Cesium')
        TypeOut("You made a Cesium bomb by mixing Cesium-137 with H2O!\n", newline=False)
        if "Hazmat Suit" in player.inventory:
            TypeOut("Thanks to your Hazmat Suit, you aren't affected by the radiation.")
        else:
            TypeOut("The radiation is toxic to your health and you take significant damage.")
            player.hp = player.hp  / 2

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
    'Empty GFUEL Shaker' : "A empty GFUEL shaker cup that once was filled with Lingonberry.",
    'PewDiePie 100M Edition Clutch Chair' : Chair,
    'Tunnel' : Tunnel,
    'Maya\'s Eyepatch' : "Return this item to Maya!",
    'Large Health Potion' : HealthPotion,
    'Small Health Potion' : HealthPotion,
    'Cesium' : Cesium,
    'Hazmat Suit' : "Protects you from radiation.\nIf you somehow managed to find any. . .",
    'Blue Ice Gfuel' : "Deliver this item to Walter White.",
    "Walter's 24\" Pizza" : "A pizza Walter White gave to you because his wife is a whore.",
    "Very yummy Hot Dog" : "You know, a like, very yummy hotdog.",
    "Dope Jacket" : "One DOPE jacket, son.",
    "Sword" : "Increased damage when attacking.",
    "Dik Whip" : "A trophy you recieved for defeating Big Dikman.\nIt has his name written on the handle.",
    "Red Key" : "Opens the Red Door.",
    "Green Key" : "Opens the Green Door.",
    "Violet Key" : "Opens the Violet Door.",
    "Orange Key" : "Opens the Orange Door.",
    "Yellow Key" : "Opens the Yellow Door.",
    "Blue Key" : "Opens the Blue Door.",
    "Indigo Key" : "Opens the Indigo Door.",
    "Gem" : "Collect all the gems and use them to open the Gemstone Door."
    }



#~/ Player \~#
class Player:
    def __init__(self):
        self.hp = 20
        self.name = GetName()
        self.inventory = ["GFUEL"]
        self.attackItems = []
        self.room = rooms[0]
        self.coins = 0
        self.quests = ["Retrieve all the gems. With all of the gems, you can open the Gemstone Door."]
        self.deaths = 0

    def TakeDamage(self, dmg):
        self.hp -= dmg
        if(self.hp <= 0):
            self.PlayerDie()

    def PlayerDie(self):
        ClearConsole()
        if "GFUEL" in player.inventory:
            TypeOut("As you are bleeding out, you remember you have GFUEL.")
            time.sleep(.5)
            TypeOut("You quickly chug it all and feel revived!")
            TypeOut("After you finish your GFUEL you quickly get up and escape with 1 hp.")
            player.inventory.remove("GFUEL")
            player.inventory.append("Empty GFUEL Shaker")
            player.hp += 1
            time.sleep(1)
            ColorPrint("0 DEATHS!", TextColor.yellow)
            player.room = rooms[0]

        else:
            self.deaths += 1
            TypeOut("You have been returned to your starting location.  You have died %g times."%(self.deaths))
            player.room = rooms[0]
            player.hp = 20
            time.sleep(2)

    def Punch(self, enemy):
        damage = random.randint(2,5)
        item = enemy.Damage(damage)
        if item: 
            self.inventory.append(item)
            try:
                if(item.CanAttack()):
                    self.attackItems.append(item)
            except:
                pass

    def Kick(self, enemy):
        item = enemy.Damage(random.randint(2,7))
        if item: 
            self.inventory.append(item)
            try:
                if(item.CanAttack()):
                    self.attackItems.append(item)
            except:
                pass

    def GoForDik(self, enemy):
        item = enemy.Damage(random.randint(0, 12))
        if item: 
            self.inventory.append(item)
            try:
                if(item.CanAttack()):
                    self.attackItems.append(item)
            except:
                pass

    def UseSword(self, enemy):
        item = enemy.Damage(random.randint(7,10))
        if item: 
            self.inventory.append(item)
            try:
                if(item.CanAttack()):
                    self.attackItems.append(item)
            except:
                pass
    
    def UseDikWhip(self, enemy):
        item = enemy.Damage(random.randint(7,12))
        if item: 
            self.inventory.append(item)
            try:
                if(item.CanAttack()):
                    self.attackItems.append(item)
            except:
                pass

    def HasSpecialAttackItems(self):
        if(self.attackItems):
            return True
        else:
            return False

player = Player()
