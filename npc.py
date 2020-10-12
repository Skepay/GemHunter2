# Contains all npcs.
#TODO: Convert to all object-oriented.
from src import *


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
            "question" : ["answers", "answer","ans"]
            }

        play = self.Greeting()
        if play:
            while len(self.pdpTrivia) > 0:
                self.Questions()
            self.GameOver()
        else:
            TypeOut('Get out of my sight. atoo I spit on you')

    
    def Greeting(self):
        ClearConsole()
        TypeOut("???: HEY BRO ITS ME, PEWDIEPIEEEEEE.\n",newline=False)
        TypeOut("PEWDIEPIE: Wanna play a little trivia?  If you win I'll give you my chair.\n",newline=False)
        playTrivia = ValidInput("(y/n)\n\n-> ","y","n")
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
        random.shuffle(list(self.pdpTrivia.items())[triviaQuestion][1]) # shuffles the original answers
        ColorPrint(list(self.pdpTrivia.items())[triviaQuestion][0])  # prints the question
        
        # print answers
        for index, answer in enumerate(list(self.pdpTrivia.items())[triviaQuestion][1]):
            print("%s. %s\n"%(index+1, answer), end = '')
        
        pdpTriviaGuess = ValidInput("-> ",answerList[0],answerList[1],answerList[2])

        if pdpTriviaGuess == answerList[0]: # if their guess was right
            self.pdpScore += 1
            TypeOut(self.RandomResponse())
            time.sleep(1)

        else:                               # if their guess was wrong
            self.pdpScore -= 1
            self.RandomResponse()
            time.sleep(1)
        del self.pdpTrivia[list(self.pdpTrivia.items())[triviaQuestion][0]]

    def GameOver(self):
        ClearConsole()
        TypeOut("PEWDIEPIE: Hm.. you finished with a score of ", 0.06, newline=False); ColorPrint(str(self.pdpScore), TextColor.yellow)
        time.sleep(1.5)

        if self.pdpScore >= 2:  # player win
            TypeOut("PEWDIEPIE: Good enough for me!\nPEWDIEPIE: Take my chair, you were like a father to me afterall..")
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

    def Greeting(self):
        TypeOut("???: H-h-h hey.  I'm Elon.")
        TypeOut("ELON MUSK:  Can you drive my roadster through these martian mountains?  I'll let you build and use the next Boring Company tunnel if you do.")
        driveRoadster = ValidInput("(y/n)\n\n->", "y", "n")
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
            direction = input('Enter direction (wasd)\n').lower()
            if direction in directions:
                if maze[player[0] + directions[direction][0]][player[1] + directions[direction][1]] != '#':
                    player[0] += directions[direction][0]
                    player[1] += directions[direction][1]
            ClearConsole()
        return True

    def GameOver(self):
        ClearConsole()
        TypeOut("ELON MUSK: Thanks, I hope the drive wasn't too bad.  Heres the access card to use the tunnel.\n", newline=False)
        ColorPrint("You have recieved a Tunnel Card.  This tunnel beings at %s", TextColor.lightpurple)
        Player.inventory.append("Tunnel Card: %s"%self.room.name)
        # Removes npc from room.
        Player.room.npc = None




#TODO: call npcs here
npc = {
    "PewDiePie" : PewDiePie,
    "BigDikman" : BigDikman,
    "Elon Musk" : Elon
}