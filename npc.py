# Contains all npcs.
#TODO: Convert to all object-oriented.
from src import *


#~/ NPCS \~#
# COLINS WEIRD GUY // BIGDIKMAN
class BigDikman:
    def __init__(self):
        self.name = self.GetDikmanName()
        self.hp = random.randint(15,20)

    def GetDikmanName(self):
        firstNawme = ["Alfred", "Charlie", "Betty", "Billy", "Hughbert", "Home", "Homie", "Cox", "Guy", "Frackles", "Adolf"]
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
            "What is the name of my signature GFUEL flavor?" : ["Lingonberry", "Red Sugar", "PewDiePie"],
            "What year was it when I reached 50,000,000 subs?" :  ["2016", "2015", "2013"],
            "What is my Wife's name?" : ["Marzia Kjellberg", "Martha Bisognin", "Merzia Kjellberg"],
            "Which games does the infamous word \"BARRELS\" come from?" : ["Amnesia", "Resident Evil", "Paranormal Activity"],
            "Before the \"9 Year olds,\" what was my fanbase called?" : ["Bro Army", "Floor Gang", "Gamers"]
            }
    
    def RandomResponse():
        pewdsResponses = ['Wonderful job!', '20% Muscle Increase', 'Big PP', '*meme review*', 'HahHAhah HOWS IT GOIN BROES.. MY NAME IS PEWWWWWWWWWWWWWWDIEPIEEHHHHHHHHHHHH', 'Code PEWDIEPIE gets you 30% off Gfuel.com']
        return random.choice(pewdsResponses)
    
    def printQuestions(self):
        ClearConsole()

        triviaQuestion = random.randint(0,len(self.pdpTrivia)-1) # gets a random question from the dictionary
        answerList = list(self.pdpTrivia.items())[triviaQuestion][1].copy() # gets the answers for that questions and copies it (first item is correct answer)
        random.shuffle(list(self.pdpTrivia.items())[triviaQuestion][1]) # shuffles the original answers
        ColorPrint(list(self.pdpTrivia.items())[triviaQuestion][0])  # prints the question
        
        # print answers
        for index, answer in enumerate(list(self.pdpTrivia.items())[triviaQuestion][1]):
            print("%s. %s"%(index, answer), end = '')

        pdpTriviaGuess = ValidInput("-> ",answerList[0],answerList[1],answerList[2])

        if pdpTriviaGuess == answerList[0]: # if their guess was right
            self.pdpScore += 1
            self.RandomResponse()
            time.sleep(1)
        else:                               # if their guess was wrong
            self.pdpScore -= 1
            self.RandomResponse()
            time.sleep(1)
    
    def GameOver(self):
        TypeOut("PEWDIEPIE: Hm.. you finished with a score of ",0.06,newline=False); ColorPrint(str(self.pdpScore), TextColor.yellow)
        
        if self.pdpScore >= 2:  # player win
            TypeOut("PEWDIEPIE: Good enough for me!\nPEWDIEPIE: Take my chair, you were like a father to me afterall..")
            ColorPrint("You recieved a PewDiePie 100M Edition Clutch Chair!", TextColor.red)
            TypeOut("To use the chair, interact with it in your inventory from the menu.")
            time.sleep(2)
            Player.inventory.append("PewDiePie 100M Edition Clutch Chair")
        
        else: # player loss
            TypeOut("PEWDIEPIE: No, you know what.. you're a sucky gamer, you can't have my chair.  Get out of my sight.")
            time.sleep(2)
        # Removes npc from room.
        Player.room.NPC = None

    
#TODO: call npcs here
npc = {
    "PewDiePie" : None,
    "BigDikman" : None,
}