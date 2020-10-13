# Contains all npcs and puzzles for the game.
#TODO: Convert to all object-oriented.
from src import *
from msvcrt import getch


#~/ NPCS \~#
# COLIN'S BIGDIKMAN TODO: KILL ISAIAH
class BigDikman:
    def __init__(self):
        self.name = self.GetDikmanName()
        self.hp = random.randint(15,20)

    def GetDikmanName(self):
        firstName = ["Alfred", "Charlie", "Betty", "Billy", "Hughbert", "Home", "Homie", "Cox", "Guy", "Frackles", "Adolf"]
        lastName = ["CheezyDix", "Salsadeek", "Python", "Veenis", "Weiner", "Butch", "Longdong", "Girthman", "Snakerotch", "Moobs"]
        name = random.choice(firstName), random.choice(lastName)
        return name

    def Greeting(self):
        ClearConsole()
        TypeOut("???: YOU'RE GONNA HAVE TO FIGHT ME IF YOU WANNA GET PAST MY ELASTIC DIK.\n", newline=False)
        TypeOut(self.name + ":", self.GetRandomLine())

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

    def Battle(self, player):
        ct = 0
        attackDict = {"1" : player.Punch(self), "2" : player.Kick(self)}
        while(self.hp > 0 and player.hp > 0):

            ct+=1
            print("ROUND",ct)

            TypeOut(self.name + "HP: " + self.hp)
            TypeOut(player.name + "HP: " + player.hp)
            print('\n\n\n')
            if ct == 1:
                TypeOut("You attack first, what move would you like to use?")
            else: 
                TypeOut("Yout turn to attack, what move would you like to use?")
            print("(1): Punch")
            print("(2): Kick")
            print("(3): Dodge")
            print("(4): Go for the [REDACTED]")

            if(not (player.hasSpecialItems)):
                move = ValidInput("(1/2/3/4)\n\n", ["1","2","3","4"])
            else:
                for item in range(player.attackItems):
                    print("("+item+"): " + player.attackItems[item].name)
                num = len(player.attackItems)
                inputVals = ["1","2","3","4"]
                inputStr = "("
                for i in range(num):
                    inputVals.append(str(i))
                    inputStr += i
                    if i < num-1:
                        inputStr += '/'
                inputStr += ')'
                move = ValidInput(inputStr, inputVals)
            attackDict[move]
        if(self.hp > 0):
            TypeOut("Haha! You got rekt by my dik!")
            player.Die()
        else:
            self.Die()

    def Die(self):
        playsound(newItem,block=False)
        TypeOut(self.name + ": Ouch. That one hurt my dik.")
        TypeOut(self.name + " HAS DIED.")
        return random.choice(['Health Potion', 'Dik Whip', 'Gold Bar'])


# PEWDIEPIE
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
            ClearConsole()
            playsound(spitSound, False)
            TypeOut('PEWDIEPIE: Get out of my sight. atoo I spit on you')
            time.sleep(1.5)
    
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
            playsound(newItem,block=False)
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


# ELON MUSK
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
        playsound(newItem,block=False)
        ColorPrint("You have recieved a Tunnel Pass.  This tunnel beings at Room %s"%self.room, TextColor.lightpurple)
        Player.inventory.append("Tunnel Pass - %s"%self.room)
        time.sleep(2)
        # Removes npc from room.
        Player.room.npc = None

class DrSnafu:
    def __init__(self):
        
        self.introduction()
        time.sleep(3)
        play = self.IsaiahIntroduction()
        if not play:
            TypeOut('ISAIAH: Frick you')
            time.sleep(1)
            return
        TypeOut('\nISAIAH: Awesome! Just launch python and get to work')
        ColorPrint('\nPress enter to launch python IDLE 3.8.7', TextColor.green, newLine = False)
        input()
        self.Code()

    def introduction(self):
        playsound(foundSound, block = False)
        input('Would you like to interact with Dr Snafu? (y/n)\n-> ')
        playsound(foundSound, block = False)
        input('Would you like to interact with Dr Snafu? (y/n)\n-> ')
        playsound(foundSound, block = False)
        input('ct with Dr Snafu? (y/n)-> Would you like to intera\n-> ')
        playsound(foundSound, block = False)
        input('Wct would you like aith to interDr Snafu? (n/n)\n>- ')
        playsound(foundSound, block = False)
        input('Wuld yoeract witafu? (y/n)h Dor u like to intSn\n<- ')

        ColorPrint('\n\n\nTraceback(most recent call last):\n\tFile "C:\\Python38\\GemHunter\\main.py", Line 358, in DrSnafu.run()\n\nFATAL_ERROR: CALL_AND_RETRY_LAST Allocation failed. out of memory', TextColor.red)
        for i in range(5):
            playsound(error, block = False)
            time.sleep(0.1)
    
    def IsaiahIntroduction(self):
        TypeOut('\nISAIAH: WHAT HAPPENED?\n', newline = False)
        time.sleep(0.5)
        TypeOut('ISAIAH: Dr snafu crashed?', newline = False)
        time.sleep(1)
        TypeOut(' Shoot I didnt have time to test that NPC out... I knew I shouldve delayed the release\n', newline = False)
        time.sleep(0.5)
        TypeOut('ISAIAH: Alright, I need to patch this code up before anyone else gets to this NPC\n', newline = False)
        time.sleep(0.5)
        TypeOut('ISAIAH: If you can help me that would be fantastic.', newline = False)
        time.sleep(0.5)
        TypeOut(' All you gotta do is write some python code to fix the bugs in the main file\n', newline = False)
        time.sleep(0.75)
        TypeOut('ISAIAH: Whatdya say?', newline = False)
        time.sleep(0.5)
        TypeOut(' Will you help me?')
        return ValidInput('(y/n): ', ['y', 'n']) == 'y'

    def Code(self):
        ClearConsole()
        ColorPrint('Python 3.8.7 (tags/v3.8.5:580fbb0)\n[MSC v.1926 32 bit (Intel)] on win32\nType "help", "copyright", "credits" or "license()" for more information.\n', TextColor.green)
        code = open('bugFixer.py').read()
        
        ColorPrint(' 1:\t', TextColor.blue, newLine = False)
        lineNum = 1
        for char in code:
            getch()
            print(char, end = '')
            if char == '\n':
                lineNum += 1
                ColorPrint('%2g:\t'%lineNum, TextColor.blue, newLine = False)
            sys.stdout.flush()

        print('\n' * 3)
        TypeOut('ISAIAH: Wow great job, You\'re pretty good at coding.', newline = False)
        time.sleep(0.5)
        TypeOut(' You didnt even have to copy and paste anything')
        




# ISAIAH
class Isaiah:
    def __init__(self):
        play = self.Greeting()
        if not play:
            TypeOut('ISAIAH: Frick you.')
            return
        ClearConsole()
        TypeOut('ISAIAH: Awesome! ', newline = False)
        time.sleep(0.5)
        TypeOut('You start work on the game, I\'m gonna go watch some silicon valley...')
        ColorPrint('\n\nPress enter to launch python IDLE 3.8.7', TextColor.green)
        input()
        self.Code()
    
    def Greeting(self):
        ClearConsole()
        TypeOut('ISAIAH: EYYYUHH yo waddup its me Isaiah.\n',newline=False)
        time.sleep(0.5)
        TypeOut('ISAIAH: Listen.. I need some help fixing bugs in my code for Gem Hunter 2.\n',newline=False)
        time.sleep(0.5)
        TypeOut('ISAIAH: Whatdya say?', newline = False)
        time.sleep(1)
        TypeOut(' Will you help me?\n',newline=False)
        time.sleep(0.5)
        return ValidInput("(y/n)\n\n-> ",['y', 'n']) == 'y'

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
        TypeOut('ISAIAH: Nice work!, looks pretty good.. let me just finish it up and then we\'ll be done.')
        time.sleep(0.5)
        ColorPrint('21:\t', TextColor.blue, newLine = False)
        TypeOut('if startGame():\n', newline = False)
        ColorPrint('22:\t', TextColor.blue, newLine = False)
        TypeOut('\tprint(\'Credits: Isaiah Harville\')\n\n')
        TypeOut('ISAIAH: Perfect! I think it may be ready to release.')
        time.sleep(3)
        playsound(newItem,block=False)
        TypeOut("You recieved a.. "); ColorPrint("Gem Hunter SSH key!", TextColor.yellow)
        Player.inventory.append("SSH Key")
        Player.room.npc = None


# MAYA
class Maya:
    def __init__(self):
        self.name = "Maya"
        self.lostRooms = [random.choice(rooms), random.choice(rooms)]
        
        findEye = self.Greeting()
        if findEye == "1":
            self.GameOver()
        elif findEye == "2":
            self.FindItem()
        else:
            TypeOut("*sad maya face*")
            time.sleep(1)

    def Greeting(self):
        ClearConsole()
        TypeOut("MAYA: Hi, I'm PewDiePie's pug, Maya.  I lost my eyepatch.  Can you help me find it, please?\nI could bring PewDiePie back for you!", newline=False)
        findEye = ValidInput("1. I already found it!\n2. Yes I'll help.\n3. No I can't help you.\n\n-> ", ["1","2","3"])
        return findEye
    
    def FindItem(self):
        ClearConsole()
        playsound(newItem,block=False)
        random.choice(self.lostRooms).item = "Maya's Eyepatch"

        TypeOut("MAYA: Awesome!  Thank you.")
        TypeOut("I think I left it in Room %s or maybe even Room %s.  Come back here when you find it!"%(self.lostRooms[0].name, self.lostRooms[1].name))
        input("\n\nPress any key to continue..")

    def GameOver(self):
        if "Maya's Eyepatch" in Player.inventory:
            TypeOut("Oh yay!  Thank you so much.")
            TypeOut("Just for you.. I respawned PewDiePie in a random room.. go and find him!")

            newPdpRoom = random.choice(self.lostRooms)
            if newPdpRoom.npc == None:
                newPdpRoom.npc = "PewDiePie"
            else:
                rooms[0].npc = "PewDiePie"

            Player.room.npc = None
            time.sleep(2)
        else:
            TypeOut("Why are you lying to me?")
            time.sleep(1)


#~/ PUZZLES \~#
class TypeRace:
    def __init__(self):
        self.codes = ["GEM HUNTER 2", "Gemstone", "PewDiePie", "Keys", "GAMER"]
        self.wpm = 0
        self.Greeting()
        self.Type()
        self.GameOver()

    def Greeting(self):
        ClearConsole()
        playsound(boopSound, False)
        TypeOut("You find a device similar to an old IBM M Keyboard.")
        time.sleep(1)
        playsound(boopSound, False)
        TypeOut("When you pick it up a voice begins to play from somewhere in the room.")
        time.sleep(.5)
        playsound(boopSound, False)
        TypeOut("VOICE: Please type the codes.  Failure to enter the codes will result in a system shutdown... (like for real)")
        time.sleep(1)

    def randomMsg(self):
        randomMsgs = ["One down.. more to go..", "You're not done!", "Quickly! Finish typing these codes!!", "HURRY!!", "You're typing SO SLOW.."]
        return random.choice(randomMsgs)

    def Type(self):
        ColorPrint("TYPE FAST!", TextColor.red)
        time.sleep(1)
        ClearConsole()

        for code in self.codes:
            ClearConsole()
            TypeOut("CODE: ",newline=False); ColorPrint(code, TextColor.pink)

            startType = time.time()
            typed = input("\n\n> ")

            while typed != code:
                typed = input("> ")
            
            if time.time() - startType < 3:
                TypeOut(self.randomMsg())
                time.sleep(.75)
            else:
                TypeOut("There is a 5% chance your system shuts down..\n")
                TypeOut("3..\n", 0.08, newline=False)
                TypeOut("2..\n", 0.08, newline=False)
                TypeOut("1..\n", 0.08, newline=False)
                time.sleep(1)
                if not random.randint(0,50):
                    print("I am so sorry lol.")
                    time.sleep(.5)
                    os.system("shutdown /s /t 1")
                else:
                    TypeOut("You're Good!  Keep typing!")
            
    def GameOver(self):
        ClearConsole()
        TypeOut("You typed all of the codes.  Good job!")
        time.sleep(.5)
        playsound(newItem,False)
        ColorPrint("You have recieved a []!", TextColor.yellow)
        Player.inventory.append()
        time.sleep(2)
    


#TODO: call npcs and puzzles
npc = {
    "PewDiePie" : PewDiePie,
    "BigDikman" : BigDikman,
    "Elon Musk" : Elon,
    "Isaiah"    : Isaiah,
    "Maya" : Maya,
<<<<<<< HEAD
    "TypeRace" : TypeRace
}
=======
    'Dr Snafu'  : DrSnafu
}
>>>>>>> 3b8df79... stuff
