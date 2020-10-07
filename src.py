import os, time, sys, subprocess, random
from color_source import ColorsFG, color, TextColor

# Source File for Gem Hunter containing all background work.

# Make sure PIL is installed
try:
    from PIL import Image
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'pillow'])
    print("Installed Pillow.")
    exit(1)
finally:
    from PIL import Image

# Valid Input function
def ValidInput(string, param1, param2, param3 = None, param4 = None, param5 = None, param6 = None):
    validInputs = [param1,param2,param3,param4,param5,param6]
    inp = str(input(string))
    
    while 1:
        if inp in validInputs:
            return inp
        inp = str(input(string))


#~/ Item Functions\~#
def Chair():
    ClearConsole()

    useChair = ValidInput('This chair can teleport you to any room.. in STYLE.\nWould you like to use it?\n(y/n)\n\n->', "y", "n")
    if useChair == "y":
        digit_list = ["0","1","2","3","4","5","6","7","8","9"]
        while True:
            ClearConsole
            teleportLocation = input("What is the number of the room you want to travel to?\n->")
            if teleportLocation not in digit_list:
                teleportLocation = input("What is the number of the room you want to travel to?\n->")
                
            elif teleportLocation in digit_list and int(teleportLocation) > 0:
                teleportLocation = int(teleportLocation)
                break
            TypeOut('Type a valid answer or I will go to\nyour house and kill your family %s'%Player.name)
            time.sleep(1)
        return teleportLocation

# Dictionary for the items
items = {
    'GFUEL' : "A tasty beverage.",
    'PewDiePie 100M Edition Clutch Chair' : "Chair"
}


#~/ Functions \~#

# Get windows username of player.
def GetName():
    return os.getlogin()


# Loading bar animation.
def LoadingBar():
    # credit JayPay
    bar = 0; loops = 0
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

        time.sleep(random.uniform(0.025,0.175))
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


#~/ Player \~#
class Player:
    name = GetName()
    inventory = ['GFUEL']
    room = 0


#~/ NPCS \~#

# PEWDIEPIE
class pewQuestion:
    question = ""
    ans1 = ""
    ans2 = ""
    ans3 = ""
    correctAns = None

def PewDiePie():
    ClearConsole()
    pewdsResponses = ['Wonderful job!', 'Edgar cammMMmMmMm', 'I rate this Gfuel/10', '*meme review*', 'HahHAhah HOWS IT GOIN BROES.. MY NAME IS PEWWWWWWWWWWWWWWDIEPIEEHHHHHHHHHHHH' ]

    TypeOut("PEWDIEPIE: Sup Gamer, would you like to participate in a trivia?  I'll give you my chair if you win.\nDo you think you have what it takes?\n",newline=False)
    playTrivia = ValidInput("(y/n)\n\n-> ", "y", "n")

    ClearConsole()

    if playTrivia != "y": # if they dont want to play the game
        print("PEWDIEPIE: Oh well, you couldn't of won anyways.. Bye bye.")
        time.sleep(1)
        return None
       
    pdpTrivia1 = pewQuestion(); pdpTrivia2 = pewQuestion(); pdpTrivia3 = pewQuestion()

    Trivia1answers = ["399.99", "420.69", "399.90"]; Trivia2answers = ["PewDiePie", "Red Sugar", "Lingonberry"]; Trivia3answers = ["2015", "2016", "2013"]
    correctAnswers = ["399.99","Lingonberry","2016"]

    pdpTrivia1.question = "What is the great price of my chair?"
    pdpTrivia1.ans1 = Trivia1answers.pop(Trivia1answers.index(random.choice(Trivia1answers))); pdpTrivia1.ans2 = Trivia1answers.pop(Trivia1answers.index(random.choice(Trivia1answers))); pdpTrivia1.ans3 = Trivia1answers.pop(Trivia1answers.index(random.choice(Trivia1answers)))
    
    pdpTrivia2.question = "What is the name of my signature GFUEL flavor?"
    pdpTrivia2.ans1 = Trivia2answers.pop(Trivia2answers.index(random.choice(Trivia2answers))); pdpTrivia2.ans2 = Trivia2answers.pop(Trivia2answers.index(random.choice(Trivia2answers))); pdpTrivia2.ans3 = Trivia2answers.pop(Trivia2answers.index(random.choice(Trivia2answers)))

    pdpTrivia3.question = "What year was it when I reached 50 million subs?"
    pdpTrivia3.ans1 = Trivia3answers.pop(Trivia3answers.index(random.choice(Trivia3answers))); pdpTrivia3.ans2 = Trivia3answers.pop(Trivia3answers.index(random.choice(Trivia3answers))); pdpTrivia3.ans3 = Trivia3answers.pop(Trivia3answers.index(random.choice(Trivia3answers)))

    pdpTrivia = [pdpTrivia1,pdpTrivia2,pdpTrivia3]

    for index, question in enumerate(pdpTrivia):
        if question.ans1 == correctAnswers[index]:
            question.correctAns = "1"
        elif question.ans2 == correctAnswers[index]:
            question.correctAns = "2"
        elif question.ans3 == correctAnswers[index]:
            question.correctAns = "3"

    # start game messages
    TypeOut('\nPEWDIEPIE: Nani da freaky deaky?!  You think you have the knowledge of the Swedes!?\n',newline=False)
    time.sleep(1)
    TypeOut("PEWDIEPIE: Well.. lets find out.")
    time.sleep(1)

    pdpScore = 0
    for question in pdpTrivia: # prints the question and takes the answer
        ClearConsole()
        ColorPrint(question.question, TextColor.green)
        print("""1. %s\n2. %s\n3. %s\n\n"""%(question.ans1,question.ans2,question.ans3))

        pdpTriviaGuess = ValidInput("-> ","1","2","3")

        if pdpTriviaGuess == question.correctAns: # if the player guessed correctly
            pdpScore += 1
            TypeOut("PEWDIEPIE: %s"%pewdsResponses.pop(pewdsResponses.index(random.choice(pewdsResponses))))
            time.sleep(1)

        else: # if the player guessed incorrectly
            pdpScore -= 1

    ClearConsole()

    TypeOut("PEWDIEPIE: Hm.. you finished with a score of ",newline=False); ColorPrint(str(pdpScore), TextColor.yellow)
    time.sleep(2)
   
    if pdpScore >= 2: # if user won
        TypeOut("PEWDIEPIE: Good enough for me!\nPEWDIEPIE: Take my chair, you were like a father to me afterall..")
        ColorPrint("You recieved a PewDiePie 100M Edition Clutch Chair!", TextColor.red)
        TypeOut("To use the chair, interact with it in your inventory from the menu.")
        time.sleep(2)
        Player.inventory.append("PewDiePie 100M Edition Clutch Chair")

    else: # if user lost
        TypeOut("PEWDIEPIE: No, you know what.. you're a sucky gamer, you can't have my chair.  Get out of my sight.")
        time.sleep(2)

    # Removes npc from room.
    Player.room.NPC = None
    
# other npcs here