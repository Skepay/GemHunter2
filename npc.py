from src import *
#~/ NPCS \~#

class BigDikman:
    def __init__(self):
        self.name = self.GetDikmanName()
        self.hp = random.randint(15,20)
    def GetDikmanName():
        firstName = ["Alfred", "Charlie", "Betty", "Billy", "Hughbert", "Home", "Homie", "Cox", "Guy", "Frackles", "Adolf"]
        lastName = ["CheezyDix", "Salsadeek", "Python", "Veenis", "Weiner", "Butch", "Longdong", "Girthman", "Snakerotch", "Moobs"]
        name = random.choice(firstName), random.choice(lastName)
        return name
    def GetRandomLine():
        lines = [f"Whats up baby cakes? Its {self.name} time!", f"{self.name} is here to give you children! Through your nose!", "Time to choke!", "Smell the cheese?", "Do you like yogurt?", "It's long dong time!", "Yeah, I have a super power. A really long [REDACTED]", "Mine is longer than yours."]
        return random.choice(lines)
    def Damage(dmg):
        self.hp -= dmg
        if(self.hp > 0):
            TypeOut(self.name + ": Hmmm. That didn't hurt, retard. Get strangled by my [REDACTED]!")
            return 0
        else:
            return self.Die()
    def Die():
        TypeOut(self.name + ": Ouch. That one hurt my dik.")
        TypeOut(self.name + " HAS DIED.")
        return random.choice(['Health Potion', 'Dik Whip', 'Gold Bar'])

# PEWDIEPIE
class pewQuestion:
    question = ""
    ans1 = ""
    ans2 = ""
    ans3 = ""
    correctAns = None

def PewDiePie():
    ClearConsole()
    pewdsResponses = ['Wonderful job!', '20% Muscle Increase', 'Big PP', '*meme review*', 'HahHAhah HOWS IT GOIN BROES.. MY NAME IS PEWWWWWWWWWWWWWWDIEPIEEHHHHHHHHHHHH', 'Code PEWDIEPIE gets you 30% off Gfuel.com']

    TypeOut("PEWDIEPIE: Sup Gamer, would you like to participate in a trivia?  I'll give you my chair if you win.  But there is a price if you lose..\nDo you think you have what it takes?\n",newline=False)
    playTrivia = ValidInput("(y/n)\n\n-> ", "y", "n")

    ClearConsole()

    if playTrivia != "y": # if they dont want to play the game
        print("PEWDIEPIE: Oh well, you couldn't of won anyways.. Bye bye")
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
    TypeOut("\nPEWDIEPIE: OMIWA SHINDERIU!!  You think you're a GAMER!?\n",newline=False)
    time.sleep(1)
    TypeOut("PEWDIEPIE: TAMBOURINE TAMBOURINE TAMBOURINE TAMBOURINE TAMBOURINE TAMBOURINE")
    startTime = time.time()
    while time.time() != startTime + 2.5:  # test this
        print(".", end = '')

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

    TypeOut("PEWDIEPIE: Hm.. you finished with a score of ",0.06,newline=False); ColorPrint(str(pdpScore), TextColor.yellow)
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


# AMONG US NPC (WHITE)
def AmongUsNPC():
    ClearConsole()

    TypeOut("WHITE: I was in navigation doing tasks, I couldn't be the impostor.")
    playAmongUs = ValidInput("Play Among Us? (y/n)\n\n-> ", "y", "n")

    if playAmongUs != "y":
        ClearConsole()
        time.sleep(1)
        TypeOut("White was not The Impostor.",0.07)
        time.sleep(1)
        ClearConsole()
        time.sleep(.35)
        return None

    ClearConsole()
    TypeOut("Vote out The Impostor.")
    time.sleep(1)

    #defense messages
    crewMatesDef = {
        "blue" : "I found yellow dead in cafeteria by the emergency meeting button.",
        "white" : "I was in navigation.",
        "red" : "I was in Admin swiping my card.",
        "cyan" :  "I was in weapons destroying the asteroids.",
        "green" : "I was starting reactor."
    }

    #select random impostor
    crewMates = ["red","green","white","blue","cyan"]
    impostor = random.choice(crewMates)

    while impostor in crewMates:
        ClearConsole()

        ColorPrint("EMERGENCY MEETING\n\n", TextColor.red)
        for mate in crewMates:
            TypeOut("%s: %s"%(mate, crewMatesDef[mate]))

        ColorPrint("VOTE", TextColor.red); ColorPrint("(%s)"%', '.join(crewMates))

        voted = ValidInput("Who is the Impostor?\n->","white","red","blue","green","cyan")

        while voted not in crewMates:
            ClearConsole()
            TypeOut("%s has already been voted out."%voted)
            voted = ValidInput("Who is the Impostor?\n->","white","red","blue","green","cyan")

        if len(crewMates) > 1:
            if voted == impostor:
                ClearConsole()
                time.sleep(1)
                TypeOut("%s was The Impostor."%voted)
                time.sleep(1.5)
                ClearConsole()
                TypeOut("Victory.  [ITEM] has been added to your inventory.")
                # give item
                return None

            else:
                ClearConsole()
                time.sleep(1)
                TypeOut("%s was not The Impostor."%voted)
                crewMates.remove(voted)
                time.sleep(1.5)

        else:
            time.sleep(1)
            TypeOut("Defeat.  %s was the Impostor."%impostor)
            time.sleep(1.5)