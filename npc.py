# Contains all npcs and puzzles for the game.
#TODO: Convert to all object-oriented.
from src import *
from msvcrt import getch

#~/ SHOP \~#
class WanderingTraveler:
    def __init__(self, player):
        ClearConsole()
        TypeOut("Wandering Traveler: Welcome to my shop!")
        time.sleep(1.25)
        self.name = "Wandering Traveler"
        self.shopItems = {
            10 : "Very yummy Hot Dog",
            15 : "Small Health Potion",
            30 : "Large Health Potion"
        }

        while 1:
            sg = self.Greeting()
            if sg:
                sg = self.Greeting()
            else:
                break
        self.Leave()
        return
    

    def Greeting(self):
        ClearConsole()
        TypeOut("Wandering Traveler: Would you like to purchase something?\n(y/n)")
        shop = ValidInput("->", ["y","n"])
        if shop == "y":
            self.Shop(player)
            ClearConsole()
            TypeOut("Wandering Traveler: Would you like to purchase something?\n(y/n)")
            shopAgain = ValidInput("->", ["y","n"])
            if shopAgain == "y":
                return 1
            return 0
        else: TypeOut("Wandering Traveler: Ok.. farewell thy lost player!"); time.sleep(1)
        return 0


    def Shop(self,player):
        ClearConsole()
        validItems = []
        
        # Print shop
        print("\tSHOP ITEMS")
        for index, key in enumerate(self.shopItems):
            print("%g. %s    $%g coins"%(index+1, self.shopItems[key], key))
            validItems.append(str(index+1))
        print("Balance: %g"%player.coins)
        print("\n")
        playsound(boopSound, block=False)
        purchase = ValidInput("What would you like to buy?\n->", validItems)
        purchase = list(self.shopItems)[int(purchase)-1]

        if purchase > player.coins:
            ClearConsole()
            playsound(boopSound, block=False)
            TypeOut("Wandering Traveler: It doesn't seem like you can afford that.")
            time.sleep(1)
            return
        
        player.coins -= purchase
        player.inventory.append(self.shopItems[purchase])
        ClearConsole()
        playsound(newItem,block=False)
        TypeOut("%s has been added to your inventory.."%self.shopItems[purchase])
        input("\n\nPress any key to continue...")
        return


    def Leave(self):
        ClearConsole()
        playsound(boopSound, block=False)
        TypeOut("Wandering Traveler: I'm off to explore some more, maybe I'll see you again!")
        for room in rooms:
            if not room.npc:
                room.npc = "Wandering Traveler"
        player.room.npc = None
        time.sleep(1.5)
        return
 


#~/ NPCS \~#
# COLIN'S BIGDIKMAN TODO: KILL ISAIAH
class BigDikman:
    def __init__(self, player):
        self.hp = random.randint(15,20)
        self.name = self.GetDikmanName()
        self.Greeting()
        self.Battle(player)


    def GetDikmanName(self):
        firstName = ["Alfred", "Charlie", "Betty", "Billy", "Hughbert", "Home", "Homie", "Cox", "Guy", "Frackles", "Adolf"]
        lastName = ["CheezyDix", "Salsadeek", "Python", "Veenis", "Weiner", "Butch", "Longdong", "Girthman", "Snakerotch", "Moobs"]
        name = (random.choice(firstName) + " " + random.choice(lastName))
        return name


    def Greeting(self):
        ClearConsole()
        TypeOut("???: YOU'RE GONNA HAVE TO FIGHT ME IF YOU WANNA GET PAST MY ELASTIC DIK.\n", newline=False)
        TypeOut((self.name, ": ", self.GetRandomLine()))
        return


    def GetRandomLine(self):
        lines = [f"Whats up baby cakes? Its {self.name} time!", f"{self.name} is here to give you children! Through your nose!", "Time to choke!", "Smell the cheese?", "Do you like yogurt?", "It's long dong time!", "Yeah, I have a super power. A really long [REDACTED]", "Mine is longer than yours."]
        return random.choice(lines)


    def Battle(self, player):
        ct = 0
        attackDict = {"1" : player.Punch, "2" : player.Kick}
        while(self.hp > 0 and player.GetHealth() > 0):
            ClearConsole()

            ct+=1
            print("ROUND",ct)

            TypeOut((self.name," HP: ", self.hp))
            TypeOut((player.name, " HP: ", player.GetHealth()))
            print('\n\n\n')
            if ct == 1:
                TypeOut("You attack first, what move would you like to use?")
            else: 
                TypeOut("Yout turn to attack, what move would you like to use?")
            print("(1): Punch")
            print("(2): Kick")
            print("(3): Dodge")
            print("(4): Go for the [REDACTED]")

            print(self.hp)

            if(not (player.HasSpecialItems())):
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
            attackDict[move](self)
            print("PRESS ANY KEY TO CONTINUE")
            getch()

        if(self.hp > 0):
            TypeOut("Haha! You got rekt by my dik!")
            player.Die()
        else:
            self.Die()


    def Damage(self, dmg):
        TypeOut(("YOU DAMAGED ", self.name, " FOR ", dmg, "."))
        self.hp -= dmg
        if(self.hp > 0):
            TypeOut((self.name, ": Hmmm. That didn't hurt, retard. Get strangled by my [REDACTED]!"))
            return 0
        else:
            return self.Die()


    def Die(self):
        playsound(newItem,block=False)
        TypeOut((self.name,": Ouch. That one hurt my dik."))
        TypeOut((self.name, "HAS DIED."))
        return random.choice(['Health Potion', 'Dik Whip', 'Gold Bar'])



# PEWDIEPIE
class PewDiePie:
    def __init__(self, player):
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
            self.GameOver(player)
        else:
            ClearConsole()
            playsound(spitSound, block=False)
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


    def GameOver(self, player):
        ClearConsole()
        TypeOut("PEWDIEPIE: Hm.. you finished with a score of ", 0.06, newline=False); ColorPrint(str(self.pdpScore), TextColor.yellow)
        time.sleep(1.5)

        if self.pdpScore >= len(list(self.pdpTrivia)):  # player win
            TypeOut("PEWDIEPIE: Good enough for me!\nPEWDIEPIE: Take my chair, you were like a father to me afterall..\nPEWDIEPIE: Be seeing you, gamer.")
            playsound(newItem,block=False)
            ColorPrint("You recieved a PewDiePie 100M Edition Clutch Chair!", TextColor.red)
            time.sleep(1)
            TypeOut("To use the chair, interact with it in your inventory from the menu.")
            player.inventory.append("PewDiePie 100M Edition Clutch Chair")
            time.sleep(2)

        else: # player loss
            TypeOut("PEWDIEPIE: No, you know what.. you're a sucky gamer, you can't have my chair.  Get out of my sight.")
            time.sleep(2)
        # Removes npc from room.
        player.room.NPC = None



# ELON MUSK
class Elon:
    def __init__(self, player):
        self.name = "Elon Musk"
        self.room = rooms.index(player.room)

        play = self.Greeting()
        if play:
            self.driveRoadster(player)
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


    def driveRoadster(self, player):
        ClearConsole()
        maze = ['########## #########', '#        #    # #  #', '#### ### #### # ## #', '#      # #       # #', '## ### #   #####   #', '#    # #####     ###', '#### # #     ###   #', '#    ### ## ##   # #', '#    # #  #  # ### #', '###### ## # #    # #', '# #     # #  ##### #', '# # ##### ##  # #  #', '#          ## # # ##', '# #############   ##', '#  #    # #   ######', '## ###    # #   #  #', '#       # ###   #  #', '####### #     #   ##', '#       ### # #    #', '####################']
        playerD = [18,11]
        while playerD != [0,10]:
            mazes = ''
            for i in range(len(maze)):
                for j in range(len(maze[i])):
                    if i == playerD[0] and j == playerD[1]:
                        mazes += '0'
                    else:
                        mazes += maze[i][j]
                mazes += '\n'
            print(mazes)
            directions = {'w':[-1,0], 's':[1,0], 'a':[0,-1], 'd':[0,1]}
            direction = input('Enter direction. (w/a/s/d)\n').lower()
            if direction in directions:
                if maze[playerD[0] + directions[direction][0]][playerD[1] + directions[direction][1]] != '#':
                    playerD[0] += directions[direction][0]
                    playerD[1] += directions[direction][1]
            ClearConsole()
        time.sleep(1)


    def GameOver(self):
        ClearConsole()
        TypeOut("ELON MUSK: Thanks, I hope the drive wasn't too bad.  Heres the access card to use the tunnel.\nELON MUSK: Bye.")
        time.sleep(.5)
        playsound(newItem,block=False)
        ColorPrint("You have recieved a Tunnel Pass.  This tunnel beings at Room %s"%self.room, TextColor.lightpurple)
        player.inventory.append("Tunnel Pass - %s"%self.room)
        time.sleep(2)
        # Removes npc from room.
        player.room.npc = None



class DrSnafu:
    def __init__(self, player):   
        self.introduction()
        time.sleep(3)
        play = self.IsaiahIntroduction()
        if not play:
            TypeOut('ISAIAH: Frick you')
            time.sleep(1)
            return
        ClearConsole()
        TypeOut('\nISAIAH: Awesome! Just launch python and get to work')
        ColorPrint('\nPress enter to launch python IDLE 3.8.7', TextColor.green, newLine = False)
        input()
        self.Code()
        ClearConsole()
        ColorPrint("You have earned 10 coins!", TextColor.yellow)
        player.coins += 10
        time.sleep(1)
        input("\n\nPress any key to continue..")
        ClearConsole()
        time.sleep(.25)
        TypeOut("Dr Snafu: WAIT! WAIT!")
        TypeOut("Dr Snafu: I wanted to thank you for fixing me.")
        time.sleep(.25)
        playsound(newItem,block=False)
        ColorPrint("Cesium-137 ", TextColor.red, newLine=False); ColorPrint("has been added to your inventory!", TextColor.yellow, newLine=False)
        player.inventory.append("Cesium")
        time.sleep(2)
        input("\n\nPress any key to continue..\n(for real this time)")
        player.room.npc = None


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
        for _ in range(5):
            playsound(error, block = False)
            time.sleep(0.1)
    

    def IsaiahIntroduction(self):
        TypeOut('\nISAIAH: WHAT HAPPENED?\n', newline = False)
        time.sleep(0.5)
        TypeOut('ISAIAH: Dr snafu crashed?', newline = False)
        time.sleep(1)
        TypeOut(' Shoot, I didnt have time to test that NPC out... I knew I should\'ve delayed the release.\n', newline = False)
        time.sleep(0.5)
        TypeOut('ISAIAH: Alright, I need to patch this code up before anyone else gets to this NPC.\n', newline = False)
        time.sleep(0.5)
        TypeOut('ISAIAH: If you can help me that would be fantastic.', newline = False)
        time.sleep(0.5)
        TypeOut(' All you gotta do is write some python code to fix the bugs in the main file.\n', newline = False)
        time.sleep(0.75)
        TypeOut('ISAIAH: Whatdya say?', newline = False)
        time.sleep(0.5)
        TypeOut(' Will you help me?\n',newline=False)
        return ValidInput('(y/n)\n\n-> ', ['y', 'n']) == 'y'


    def Code(self):
        ClearConsole()
        ColorPrint('Python 3.8.7 (tags/v3.8.5:580fbb0)\n[MSC v.1926 32 bit (Intel)] on win32\nType "help", "copyright", "credits" or "license()" for more information.\n', TextColor.green)
        code = open(r"files\drSnafu.txt").read()
        
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
        TypeOut(' You didnt even have to copy and paste anything!')
        time.sleep(1)



# MAYA
class Maya:
    def __init__(self, player):
        self.name = "Maya"
        self.lostRooms = [random.choice(rooms), random.choice(rooms)]
        
        findEye = self.Greeting()
        if findEye == "1":
            self.GameOver(player)
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
        time.sleep(1)
        ColorPrint("You have recieved a new quest!  View it from your menu.", TextColor.yellow)
        player.quests.append("Find Maya's eyepatch. (Room %s / Room %s)"%(self.lostRooms[0].name, self.lostRooms[1].name))
        input("\n\nPress any key to continue..")


    def GameOver(self,player):
        if "Maya's Eyepatch" in player.inventory:
            TypeOut("Oh yay!  Thank you so much.")
            TypeOut("Just for you.. I respawned PewDiePie in a random room.. go and find him!")

            for room in rooms:
                if not room.npc:
                    room.npc = "PewDiePie"

            player.room.npc = None
            time.sleep(2)
        else:
            TypeOut("Why are you lying to me?")
            time.sleep(1)



class MrWhite:
    def __init__(self, player):
        if 'Blue Ice Gfuel' not in player.inventory:
            while True:
                gfuelLocation = rooms.index(random.choice(rooms))
                if not rooms[gfuelLocation].item and not rooms[gfuelLocation].door:
                    rooms[gfuelLocation].item = 'Blue Ice Gfuel'
                    break
            
            self.Greeting(gfuelLocation)
        else:
            self.ReturnGfuel()


    def Greeting(self, gfuelRoomLocation):
        ClearConsole()
        playsound(boopSound,block=False)
        TypeOut("Walter White: Jesse, I need you to bring me my Blue Ice, Jesse.")
        time.sleep(1)
        playsound(boopSound,block=False)
        TypeOut("Walter White: Oh, wait, you're not Jesse!\n",newline=False); time.sleep(.5)
        time.sleep(1)
        playsound(phoneRing,block=False)
        TypeOut("*Heisenberg's phone rings*\n",newline=False)
        TypeOut("Heisenberg: Argh, it is my whore wife Skyler.. listen, I need you to bring me my Blue Ice!!")
        time.sleep(1)
        playsound(boopSound,block=False)
        TypeOut("Heisenberg: This is not a negotiation."); time.sleep(1)
        playsound(boopSound,block=False)
        ColorPrint("You have recieved a new quest!  View it from your menu.", TextColor.yellow)
        playsound(newItem,block=False)
        player.quests.append("Get Walter White's Blue Ice from Room %g and deliver it to him."%gfuelRoomLocation.name)
        input("\n\nPress any key to continue..")


    def ReturnGfuel(self):
        ClearConsole()
        player.inventory.remove("Blue Ice Gfuel")
        playsound(boopSound,block=False)
        TypeOut("Walter White: Thank you.  My junkie partner misplaced it, I'm sorry for raising my voice earlier.")
        playsound(boopSound,block=False)
        TypeOut("Walter White: Here is this pizza, I was going to give it to Skyler, but shes a whore.")
        player.inventory.append("Walter's 24\" Pizza")
        playsound(newItem,block=False)
        ColorPrint("You have recieved Walter White's Pizza!", TextColor.yellow)
        time.sleep(1.5)
        TypeOut("Walter White: Satisfaction Guaranteed.. or its on the house!")
        time.sleep(2)


#~/ PUZZLES \~#
class TypeRace:
    def __init__(self, player):
        self.codes = ["GEM HUNTER 2", "Gemstone", "Computer", "Keys", "Labrynth", "Trapped", "No Exit"]
        self.wpm = 0
        self.Greeting()
        self.Type()
        self.GameOver(player)


    def Greeting(self):
        ClearConsole()
        playsound(boopSound, block=False)
        TypeOut("The room you walk into is surprisingly modern, unlike the other rooms you have been in.")
        playsound(boopSound, block=False)
        TypeOut("It appears to be the old control room for the labrynth you are helplessly condemned to.")
        playsound(boopSound, block=False)
        TypeOut("You find a device similar to a keyboard.. except with a lot of keys...")
        time.sleep(1)
        playsound(boopSound, block=False)
        TypeOut("When you pick it up a voice begins to play from somewhere in the room.")
        time.sleep(.5)
        playsound(boopSound, block=False)
        TypeOut("VOICE: Please type the codes.  Failure to enter the codes in time could result in a system failure.")
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
                TypeOut("Memory error. . .\n", random.uniform(0.4, 1.0))
                TypeOut("3..\n", 0.08, newline=False)
                TypeOut("2..\n", 0.08, newline=False)
                TypeOut("1..\n", 0.08, newline=False)
                time.sleep(1)
                if not random.randint(0,50):
                    ClearConsole()
                    time.sleep(10)
                    TypeOut("Back online.")
                    time.sleep(1)
                    ClearConsole()
                else:
                    TypeOut("Fixed.  Continue..")
            
            
    def GameOver(self, player):
        ClearConsole()
        TypeOut("You typed all of the codes.  Good job!")
        time.sleep(.5)
        playsound(newItem,False)
        ColorPrint("You have recieved a Hazmat Suit!", TextColor.yellow)
        player.room.npc = None
        player.inventory.append("Hazmat Suit")
        time.sleep(2)
    


#TODO: call npcs and puzzles
npc = {
    "Wandering Traveler" : WanderingTraveler,
    "PewDiePie" : PewDiePie,
    "BigDikman" : BigDikman,
    "Elon Musk" : Elon,
    "Maya" : Maya,
    "Computer" : TypeRace,
    "Dr Snafu" : DrSnafu,
    "Walter White" : MrWhite
}
