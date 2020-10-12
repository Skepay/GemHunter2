# Contains all npcs.
#TODO: Convert to all object-oriented.
from src import *
from msvcrt import getch


#~/ NPCS \~#
# COLIN'S BIGDIKMAN TODO: TEST
class BigDikman:
    def __init__(self):
        self.name = self.GetDikmanName()
        self.hp = random.randint(15,20)

    def GetDikmanName(self):
        firstName = ["Alfred", "Charlie", "Betty", "Billy", "Hughbert", "Home", "Homie", "Cox", "Guy", "Frackles", "Adolf"]
        lastName = ["CheezyDix", "Salsadeek", "Python", "Veenis", "Weiner", "Butch", "Longdong", "Girthman", "Snakerotch", "Moobs"]
        name = random.choice(firstName), random.choice(lastName)
        return name

    def GetRandomLine(self):
        lines = [f"Whats up baby cakes? Its {self.name} time!", f"{self.name} is here to give you children! Through your nose!", "Time to choke!", "Smell the cheese?", "Do you like yogurt?", "It's long dong time!", "Yeah, I have a super power. A really long [REDACTED]", "Mine is longer than yours."]
        return random.choice(lines)

    def Damage(self, dmg):
        self.hp -= dmg
        if(self.hp > 0):
            TypeOut(self.name + ": Hmmm. That didn't hurt, retard. Get strangled by my [REDACTED]!")
            return 0
        else:
            return self.Die()

    def Die(self):
        TypeOut(self.name + ": Ouch. That one hurt my dik.")
        TypeOut(self.name + " HAS DIED.")
        return random.choice(['Health Potion', 'Dik Whip', 'Gold Bar'])


# PEWDIEPIE TODO: TESTTTTTT
class PewDiePie:
    def __init__(self):
        self.name = "PewDiePie"
        self.pdpScore = 0
        self.pdpTrivia = {
            "What is the great price of my chair?" : ["399.99", "420.69", "399.90"],
            "What is the name of my signature GFUEL flavor?" : ["Lingonberry", "Swedish Meatballs", "Pewds"],
            "What year was it when I reached 50,000,000 subs?" :  ["2016", "2015", "2013"],
            "What is my Wife's name?" : ["Marzia Kjellberg", "Martha Bisognin", "Merzia Kjellberg"],
            "Which games does the infamous word \"BARRELS\" come from?" : ["Amnesia", "Resident Evil", "Paranormal Activity"],
            "Before the \"9 Year olds,\" what was my fanbase called?" : ["Bro Army", "Floor Gang", "Gamers"],
            "Where am I from?" : ["Sweden", "America", "UK"]
            }

        play = self.Greeting()
        if play:
            while len(self.pdpTrivia) > 0:
                self.Questions()
            self.GameOver()
        else:
            TypeOut('PEWDIEPIE: Get out of my sight. atoo I spit on you')

    
    def Greeting(self):
        ClearConsole()
        TypeOut("???: HEY BRO ITS ME, PEWDIEPIEEEEEE.\n",newline=False)
        TypeOut("PEWDIEPIE: Wanna play a little trivia?  If you win I'll give you my chair.\n",newline=False)
        playTrivia = ValidInput("(y/n)\n\n-> ",["y","n"])
        if playTrivia == "y":
            return True # play
        return False # dont play

    def RandomResponse(self):
        pewdsResponses = ['Wonderful job!', '20% Muscle Increase', 'Big PP', '*meme review*', 'HahHAhah HOWS IT GOIN BROES.. MY NAME IS PEWWWWWWWWWWWWWWDIEPIEEHHHHHHHHHHHH', 'Code PEWDIEPIE gets you 30% off Gfuel.com']
        return random.choice(pewdsResponses)
    
    def Questions(self):
        ClearConsole()

        triviaQuestion = random.randint(0,len(self.pdpTrivia)-1) # gets a random question from the dictionary
        answerList = list(self.pdpTrivia.items())[triviaQuestion][1].copy() # gets the answers for that questions and copies it (first item is correct answer)
        random.shuffle(list(self.pdpTrivia.items())[triviaQuestion][1]) # shuffles the original answers TODO: it doesnt shuffle
        ColorPrint(list(self.pdpTrivia.items())[triviaQuestion][0])  # prints the question
        
        # print answers
        for index, answer in enumerate(list(self.pdpTrivia.items())[triviaQuestion][1]):
            print("%s. %s\n"%(index+1, answer), end = '')
        
        pdpTriviaGuess = ValidInput("\n-> ",[answerList[0],answerList[1],answerList[2]])

        if pdpTriviaGuess == answerList[0]: # if their guess was right
            self.pdpScore += 1
            TypeOut(self.RandomResponse())
            time.sleep(1)

        else:                               # if their guess was wrong
            self.pdpScore -= 1
            TypeOut(self.RandomResponse())
            time.sleep(1)
        del self.pdpTrivia[list(self.pdpTrivia.items())[triviaQuestion][0]]

    def GameOver(self):
        ClearConsole()
        TypeOut("PEWDIEPIE: Hm.. you finished with a score of ", 0.06, newline=False); ColorPrint(str(self.pdpScore), TextColor.yellow)
        time.sleep(1.5)

        if self.pdpScore >= len(list(self.pdpTrivia)):  # player win
            TypeOut("PEWDIEPIE: Good enough for me!\nPEWDIEPIE: Take my chair, you were like a father to me afterall..\nPEWDIEPIE: Be seeing you, gamer.")
            ColorPrint("You recieved a PewDiePie 100M Edition Clutch Chair!", TextColor.red)
            time.sleep(1)
            TypeOut("To use the chair, interact with it in your inventory from the menu.")
            Player.inventory.append("PewDiePie 100M Edition Clutch Chair")
            time.sleep(2)

        else: # player loss
            TypeOut("PEWDIEPIE: No, you know what.. you're a sucky gamer, you can't have my chair.  Get out of my sight.")
            time.sleep(2)
        # Removes npc from room.
        Player.room.NPC = None


# ELON MUSK TODO: test
class Elon:
    def __init__(self):
        self.name = "Elon Musk"
        self.room = rooms.index(Player.room)

        play = self.Greeting()
        if play:
            self.driveRoadster()
            self.GameOver()
        else:
            TypeOut("ELON MUSK: ...")


    def Greeting(self):
        ClearConsole()
        TypeOut("???: H-h-h hey.  I'm Elon.\n",newline=False)
        TypeOut("ELON MUSK:  Can you drive my roadster through these martian mountains?  I'll let you build and use the next Boring Company tunnel if you do.\n",newline=False)
        driveRoadster = ValidInput("(y/n)\n\n-> ", ["y", "n"])
        if driveRoadster == "y":
            return True # play
        return False # dont play

    def driveRoadster(self):
        ClearConsole()
        maze = ['########## #########', '#        #    # #  #', '#### ### #### # ## #', '#      # #       # #', '## ### #   #####   #', '#    # #####     ###', '#### # #     ###   #', '#    ### ## ##   # #', '#    # #  #  # ### #', '###### ## # #    # #', '# #     # #  ##### #', '# # ##### ##  # #  #', '#          ## # # ##', '# #############   ##', '#  #    # #   ######', '## ###    # #   #  #', '#       # ###   #  #', '####### #     #   ##', '#       ### # #    #', '####################']
        player = [18,11]
        while player != [0,10]:
            mazes = ''
            for i in range(len(maze)):
                for j in range(len(maze[i])):
                    if i == player[0] and j == player[1]:
                        mazes += '0'
                    else:
                        mazes += maze[i][j]
                mazes += '\n'
            print(mazes)
            directions = {'w':[-1,0], 's':[1,0], 'a':[0,-1], 'd':[0,1]}
            direction = input('Enter direction. (w/a/s/d)\n').lower()
            if direction in directions:
                if maze[player[0] + directions[direction][0]][player[1] + directions[direction][1]] != '#':
                    player[0] += directions[direction][0]
                    player[1] += directions[direction][1]
            ClearConsole()
        time.sleep(1)

    def GameOver(self):
        ClearConsole()
        TypeOut("ELON MUSK: Thanks, I hope the drive wasn't too bad.  Heres the access card to use the tunnel.\nELON MUSK: Bye.")
        time.sleep(.5)
        ColorPrint("You have recieved a Tunnel Pass.  This tunnel beings at Room %s"%self.room, TextColor.lightpurple)
        Player.inventory.append("Tunnel Pass - %s"%self.room)
        time.sleep(2)
        # Removes npc from room.
        Player.room.npc = None

class Isaiah:
    def __init__(self):
        play = self.Greeting()
        if not play:
            TypeOut('Isaiah: Frick you')
            return
        TypeOut('Isaiah: Awesome! ', newline = False)
        time.sleep(0.5)
        TypeOut('You start work on the game, Im gonna go put my name in the credits and then watch some silicon valley...')
        ColorPrint('\n\n\nPress enter to launch python IDLE 3.8.7', TextColor.green)
        input()
        self.Code()
    
    def Greeting(self):
        ClearConsole()
        TypeOut('Isaiah: EYYYUHH yo waddup its me Isaiah')
        time.sleep(0.5)
        print('        ', end = '')
        TypeOut('Listen... I need some help fixing bugs in my poopy code for Gem Hunter 2')
        time.sleep(0.5)
        print('        ', end = '')
        TypeOut('Whatdya say? ', newline = False)
        time.sleep(1)
        TypeOut('will you help me?')
        time.sleep(0.5)
        print('')
        return ValidInput("(y/n)\n-> ",['y', 'n']) == 'y'

    def Code(self):
        ClearConsole()
        ColorPrint('Python 3.8.7 (tags/v3.8.5:580fbb0)\n[MSC v.1926 32 bit (Intel)] on win32\nType "help", "copyright", "credits" or "license()" for more information.\n\n\n', TextColor.green)
        code = '\n'.join(open('main.py').read().split('\n')[:20])
        lineNum = 1
        ColorPrint('1:\t', TextColor.blue, newLine = False)
        for char in code:
            getch()
            print(char, end='')
            if char == '\n':
                lineNum += 1
                ColorPrint('%g:\t'%lineNum, TextColor.blue, newLine = False)
            sys.stdout.flush()
        print('\n' * 3)
        TypeOut('Isaiah: Nice work!, looks pretty good... let me just finish it up and then we\'ll be done')
        time.sleep(0.5)
        ColorPrint('21:\t', TextColor.blue, newLine = False)
        TypeOut('if startGame():', newLine = False)
        ColorPrint('22:\t', TextColor.blue, newLine = False)
        TypeOut('\tprint(\'Credits: Isaiah Harville\')\n\n')
        TypeOut('Isaiah: Perfect! I think it may be ready to release')



# MAYA
class Maya:
    def __init__(self):
        self.name = "Maya"
        
        play = self.Greeting()
        if play == 1:
            pass
        elif play == 2:
            if "Maya's Eyepatch" in Player.inventory:
                TypeOut("Oh yay!  Thank you so much.")
            else:
                TypeOut("Why are you lying to me?")
                time.sleep(1)
        else:
            TypeOut("*sad maya face*")
            time.sleep(1)


    def Greeting(self):
        TypeOut("MAYA: Hi, I'm PewDiePie's pug.  I lost my eyepatch.  Can you help me find it please?\n", newline=False)
        findEye = ValidInput("1. I already found it!\n2. Yes I'll help.\n3. No I can't help you.\n\n-> ", ["1","2","3"])
        return findEye
    
    def FindItem(self):
        ClearConsole()
        room1 = random.choice(rooms)
        room2 = random.choice(rooms)

        TypeOut("MAYA: Awesome!  Thank you.")
        TypeOut("I think I left it in Room %s or maybe Room %s.  Come back here when you find it!"%(room1.name, room2.name))
        time.sleep(3)

    def GameOver(self):
        pass


#TODO: call npcs here
npc = {
    "PewDiePie" : PewDiePie,
    "BigDikman" : BigDikman,
    "Elon Musk" : Elon,
    "Isaiah"    : Isaiah
}