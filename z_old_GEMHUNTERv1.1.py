import os
import sys
import time
import random
#TODO: puzzles, more mpcs, more content, search room func, with search room loading bar (15 second).  Save file, NPC's that can grant keys,use colors
"""
memory comments:
#GOALS: Save file, NPC's that can grant keys,
#DICTIONARIES: 1 for each of the 4 rooms
#THIS IS A DOUBLE CLICK TO PLAY GAME!  DO NOT EDIT WITH IDLE
"""

#|=-=-=| Functions |=-=-=|#
# PrintInventory
def PrintInventory():
    InventoryString = ', '.join(player['Inventory'])
    print('\033[0;33mYour inventory includes: %s\033[00m'%InventoryString)


# Print Possible Directions 
def PrintPossibleDirections():
    movements = []
    for i in locations[player['Room']]:
        if type(locations[player['Room']][i]) == int:
            movements.append(i)
    movements = ', '.join(movements)
    print('Your possible movements are: %s'%movements)


# Find Item
def FindItem():
    os.system('cls')
    print ('\033[0;33mYou found a %s\033[0;33m!\033[00m'%locations[player['Room']]['Items']) #TODO: experiment with slow color
    input('')
    os.system('cls')
    player['Inventory'].append(locations[player['Room']]['Items'])
    locations[player['Room']]['Items'] = None


# GetName
def GetName():
    return os.getlogin()


# Welcome message
def WelcomeUser():
    player['Name'] = GetName()
    TypeOut('Welcome %s, to the text based adventure game...'%player['Name'])
    time.sleep(0.5)
    TypeOut('G E M    H U N T E R',0.06)
    input('')
    os.system('cls')


# TypeOut
def TypeOut(str, pause = 0.045, newline = True):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(pause)
    if newline:
        print("\n")


# NPC Messages
def NPCtalk(NPC):
    time.sleep(1)
    for i in NPC['Messages']:
        TypeOut(i)
        time.sleep(0.3)


# Can Make Rainbow Gem
def CanMakeRainbowKey():
    for i in gems:
        if i not in player['Inventory']:
            return False
    return True

def MakeRainbowKey():
    for i in gems:
        player['Inventory'].remove(i)
    player['Inventory'].append('\033[1;31;40mR\033[1;33;40mA\033[1;33;40mI\033[1;32;40mN\033[1;34;40mB\033[1;35;40mO\033[1;31;40mW  \033[00mKEY')
    TypeOut('Congratuations %s!  You have successfully collected all of them gems!!'%player['Name'])
    time.sleep(3)
    print('\033[0;33mSuddenly, your chair comes and sweeps you off your feet!  You feel a buldge in your pants grow.. and suddenly\nthe gems FLY OUT OF YOUR PANTS AND INTO THE AIR!\nThe gems begin to fuse together and you earn a \033[1;31;40mR\033[1;33;40mA\033[1;33;40mI\033[1;32;40mN\033[1;34;40mB\033[1;35;40mO\033[1;31;40mW  \033[00mKEY\033[0;00m')
    input()
    TypeOut('CREDITS',0.06) #TODO: CLEAR THIS CRAP UP
    time.sleep(1)
    os.system('cls')
    TypeOut('Love to GEM HUNTER v1.')

#|=-=-=| NPCS |=-=-=|#
# Wizard Rock Paper scissors
def RPS():
    TypeOut('\nAha! You dare challenge me? Im a master at this game')
    weapons = ['Rock','Paper','Scissors']
    while True:
        print('\033[0;33mChoose Your Weapon:\n1: Rock\n2: Paper\n3: Scissors\033[00m')
        try:
            weaponchoice = int(input(''))-1
        except:
            print('\033[0;33mPlease enter a valid choice\033[00m')
            continue
        wizardweapon = random.randint(0,2)
        TypeOut('\nI chose %s!'%weapons[wizardweapon])
        if wizardweapon == weaponchoice:
            TypeOut('We tie! lets try this again shall we?')
        else:
            break

    win = True
    if wizardweapon == 0 and weaponchoice == 2:
        win = False
    elif wizardweapon == 1 and weaponchoice == 0:
        win = False
    elif wizardweapon == 2 and weaponchoice == 1:
        win = False
    if win:
        TypeOut('\nDrats! You win')
        TypeOut('I am a Wizard of my word so here is the gem I promised')
        while True:
            ri = random.randint(0,len(gems)-1)
            if gems[ri] not in player['Inventory']:
                player['Inventory'].append(gems[ri])
                print ('\033[0;33mYou found a %s\033[0;33m!\033[00m'%gems[ri])
                gemlocations[ri]['Items'] = None
                break
    else:
        TypeOut('\nI warned you... I am the best!')
        time.sleep(1)
        player['Room'] = 0


# PewDiePie
#TODO: finish question
class questions:
    pass

question1 = dict([
            ('question','What is my full name?!?'),
            ('ans1','Felix Arvid Ulf Kjellberg'),
            ('ans2','Felix Alvin Dam Kjelbeg'),
            ('ans3','Felix Arvid Ulf Kjelberg')
            ])

question2 = dict([
            ('question','What code do you use to get 30% on Gfuel?'),
            ('ans1','PewDiePie'),
            ('ans2','Lingonberry'),
            ('ans3','IMRTS')
            ])

question3 = dict([
            ('question','What is the great price of my chair?'),
            ('ans1','$399.99'),
            ('ans2','$420.69'),
            ('ans3','$399.90')
            ])

question4 = dict([
            ('question','Who is the best YouTuber?'),
            ('ans1','PewDiePie'),
            ('ans2','Idubzzz'),
            ('ans3','Jacksepticeye')
            ])

question5 = dict([
            ('question','What is my wifes name?'),
            ('ans1','Marzia'),
            ('ans2','Marcia'),
            ('ans3','Maria')
            ])

question6 = dict([
            ('question','Which of these games have I never played on camera?'),
            ('ans1','Resident Evil 7'),
            ('ans2','The Sims 3'),
            ('ans3','Slender')
            ])

question7 = dict([
            ('question','Is math related to science?'),
            ('ans1','applesauce'),
            ('ans2','no'),
            ('ans3','yes')
            ])

question8 = dict([
            ('question','What is the 18th word I said in video #9 of my minecraft series?'),
            ('ans1','Sven'),
            ('ans2','time'),
            ('ans3','week')
            ])

questionlist = [question1, question2, question3, question4, question5, question6, question7, question8]

def pewds():
    responselist = ['Wonderful job!', 'Ahh.. penis music to my ears..', 'I rate this Gfuel/10', 'SKRATTA DUE FORLORA DUE MAAAAAAAAAAAAAAAAAAAAAAANNEEEEEEEEEEEEEEEEN', '*meme review*', '..hey congratulations, its a celebration..', 'BARRELS', 'HahHAhah HOWS IT GOIN BROES.. MY NAME IS PEWWWWWWWWWWWWWWDIEPIEEHHHHHHHHHHHH' ]
    win = True
    os.system('cls')

    TypeOut('\nNani da freaky deaky?!  You think you know the knowledge of the Swedes!?')

    for i in range(len(questionlist)):
        aq = random.randint(0,len(questionlist)-1)
        question = questionlist.pop(aq)
        print('\033[0;33m%s\n'%question['question'])
        answerlist = ['ans1','ans2','ans3']
        random.shuffle(answerlist)

        for i in range(len(answerlist)):
            print('\033[0;33m%g. %s'%(i+1,question[answerlist[i]]))
            print('\033[0;00m')

        while True:
            try:
                UserAnswer = int(input(''))
                if UserAnswer in range(1,4):
                    break
                else:
                    TypeOut('Thats not a valid number...')
                    TypeOut('Type a valid answer or I will go to\nyour house and kill your family %s'%player['Name'])
            except:
                TypeOut('Thats not a valid answer...')
                TypeOut('Type a valid answer or I will go to\nyour house and kill your family %s'%player['Name'])

        if answerlist[UserAnswer-1] != 'ans1':
            win = False
            TypeOut('Wow, Im dissapointed... I thought you were a real gamer  for a second... I guess I was wrong.\nYou have a small pp after all, %s'%player['Name'])
            break

        else:
            TypeOut(responselist.pop(aq))
        input('')
        os.system('cls')
    if win:
        TypeOut('Wow! Im impressed, you clearly have a huge pp.. take my chair, you deserve it.\n ..you are like a father to me.. UwU')
        player['Inventory'].append('PewDiePie Chair')
        print ('\033[0;33mYou recieved a \033[0;31mPewDiePie 100M Edition Clutch Chair\033[0;33m!\033[00m')
        TypeOut('To use the chair, type "Mr Chair" instead of your tradiational direction inputs')
        TypeOut('After that, you will be able to choose which room you would like to teleport to')

# NPCS
Wizard = dict([
            ('Name','A Wizard'),
            ('Messages',['Greetings %s'%GetName(),
                         'Id like to make a deal with you',
                         'You see, Im a master at rock paper scissors',
                         'If you can beat me, Ill grant you a random gem',
                         'But if you lose...',
                         'Ill return you to Room 0']),
            ('YON','Would you like to take the Wizards deal? (y/n)'),
            ('Yes',RPS),
            ('No','\nAh, very well... btw u gay')
            ])


pdp = dict([
            ('Name', 'PewDiePie'),
            ('Messages',['What is up gamer?',
            'If you can answer a couple of questions Ill lend you my chair.',
            'If you are rocking this chair, you can teleport to any room of your choice.',
            'So.. the question is, do you have a big pp or a small pp?']),
            ('YON','Would you like to take the PewDiePie trivia? (y/n)'),
            ('Yes',pewds),
            ('No','\nJust as well, only true gamers can answer my questions')
           ])


# DOORS
RedDoor = dict([
            ('Name','\033[0;31mRed Door\033[00m'),
            ('Requires','\033[0;31mRed Key\033[00m')
            ])

OrangeDoor = dict([
            ('Name','\033[0;33mOrange Door\033[00m'),
            ('Requires','\033[0;33mOrange Key\033[00m')
            ])

YellowDoor = dict([
            ('Name','\033[0;33mYellow Door\033[00m'),
            ('Requires','\033[0;33mYellow Key\033[00m')
            ])

GreenDoor = dict([
            ('Name','\033[0;32Green Door\033[00m'),
            ('Requires','\033[0;32mGreen Key\033[00m')
            ])

BlueDoor = dict([
            ('Name','\033[0;34mBlue Door\033[00m'),
            ('Requires','\033[0;34mBlue Key\033[00m')
            ])

PurpleDoor = dict([
            ('Name','\033[35mPurple Door\033[00m'),
            ('Requires','\033[0;35mPurple Key\033[00m')
            ])

################################################################################|RAINBOW DOOR DICTIONARY
RainbowDoor = dict([
            ('Name','\033[1;31;40mR\033[1;33;40mA\033[1;33;40mI\033[1;32;40mN\033[1;34;40mB\033[1;35;40mO\033[1;31;40mW\033[00m DOOR'),
            ('Requires','\033[1;31;40mR\033[1;33;40mA\033[1;33;40mI\033[1;32;40mN\033[1;34;40mB\033[1;35;40mO\033[1;31;40mW  \033[00mKEY')
            ])

################################################################################|ROOM 0 DICTIONARY
room0 = dict([
            ('Name','Room 0'),
            ('Items',None),
            ('Up',2),
            ('Down',85),
            ('Left',1),
            ('Right',3),
            ('Doors',['Down',RainbowDoor]),
            ('NPC',None)
            ])

################################################################################|ROOM 1 DICTIONARY
room1 = dict([
			('Name', 'Room 1'),
			('Items',None),
			('Up',4),
			('Down',None),
			('Left',8),
			('Right',0),
            ('Doors',['Up',BlueDoor]),
            ('NPC',None)
			])

################################################################################|ROOM 2 DICTIONARY
room2 = dict([
            ('Name','Room 2'),
            ('Items',None),
			('Up',35),
			('Down',0),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|ROOM 3 DICTIONARY
room3 = dict([
            ('Name','Room 3'),
            ('Items','\033[0;34mBlue Key\033[00m'),
			('Up',None),
			('Down',19),
			('Left',0),
			('Right',24),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|ROOM 4 DICTIONARY
room4 = dict([
            ('Name','Room 4'),
            ('Items','\033[0;34mBlue gemstone\033[00m'),
			('Up',7),
			('Down',1),
			('Left',5),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room5 = dict([
            ('Name','Room 5'),
            ('Items',None),
			('Up',6),
			('Down',None),
			('Left',None),
			('Right',4),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room6 = dict([
            ('Name','Room 6'),
            ('Items',None),
			('Up',None),
			('Down',5),
			('Left',41),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room7 = dict([
            ('Name','Room 7'),
            ('Items',None),
			('Up',None),
			('Down',4),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room8 = dict([
            ('Name','Room 8'),
            ('Items',None),
			('Up',None),
			('Down',11),
			('Left',9),
			('Right',1),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room9 = dict([
            ('Name','Room 9'),
            ('Items',None),
			('Up',10),
			('Down',None),
			('Left',None),
			('Right',8),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room10 = dict([
            ('Name','Room 10'),
            ('Items','\033[0;33mYellow Key\033[00m'),
			('Up',None),
			('Down',9),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room11 = dict([
            ('Name','Room 11'),
            ('Items',None),
			('Up',8),
			('Down',None),
			('Left',None),
			('Right',12),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room12 = dict([
            ('Name','Room 12'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',11),
			('Right',13),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room13 = dict([
            ('Name','Room 13'),
            ('Items',None),
			('Up',None),
			('Down',14),
			('Left',12),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room14 = dict([
            ('Name','Room 14'),
            ('Items',None),
			('Up',13),
			('Down',None),
			('Left',None),
			('Right',15),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room15 = dict([
            ('Name','Room 15'),
            ('Items',None),
			('Up',None),
			('Down',21),
			('Left',14),
			('Right',16),
            ('Doors',['Down',RedDoor]),
            ('NPC',None)
            ])

################################################################################|
room16 = dict([
            ('Name','Room 16'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',15),
			('Right',17),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room17 = dict([
            ('Name','Room 17'),
            ('Items',None),
			('Up',18),
			('Down',None),
			('Left',16),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room18 = dict([
            ('Name','Room 18'),
            ('Items',None),
			('Up',None),
			('Down',17),
			('Left',None),
			('Right',19),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room19 = dict([
            ('Name','Room 19'),
            ('Items',None),
			('Up',3),
			('Down',20),
			('Left',18),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room20 = dict([
            ('Name','Room 20'),
            ('Items',None),
			('Up',19),
			('Down',None),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room21 = dict([
            ('Name','Room 21'),
            ('Items',None),
			('Up',15),
			('Down',None),
			('Left',22),
			('Right',23),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room22 = dict([
            ('Name','Room 22'),
            ('Items','\033[0;31mRed gemstone\033[00m'),
			('Up',None),
			('Down',None),
			('Left',None),
			('Right',21),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room23 = dict([
            ('Name','Room 23'),
            ('Items','\033[0;32mGreen Key\033[00m'),
			('Up',None),
			('Down',None),
			('Left',21),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room24 = dict([
            ('Name','Room 24'),
            ('Items',None),
			('Up',None),
			('Down',25),
			('Left',3),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room25 = dict([
            ('Name','Room 25'),
            ('Items',None),
			('Up',24),
			('Down',26),
			('Left',None),
			('Right',27),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room26 = dict([
            ('Name','Room 26'),
            ('Items',None),
			('Up',25),
			('Down',None),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room27 = dict([
            ('Name','Room 27'),
            ('Items',None),
			('Up',33),
			('Down',28),
			('Left',25),
			('Right',29),
            ('Doors',['Down',YellowDoor]),
            ('NPC',None)
            ])

################################################################################|
room28 = dict([
            ('Name','Room 28'),
            ('Items','\033[0;33mYellow gemstone\033[00m'),
			('Up',27),
			('Down',None),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room29 = dict([
            ('Name','Room 29'),
            ('Items',None),
			('Up',30),
			('Down',None),
			('Left',27),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room30 = dict([
            ('Name','Room 30'),
            ('Items',None),
			('Up',31),
			('Down',29),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room31 = dict([
            ('Name','Room 31'),
            ('Items',None),
			('Up',None),
			('Down',30),
			('Left',32),
			('Right',34),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room32 = dict([
            ('Name','Room 32'),
            ('Items',None),
			('Up',None),
			('Down',33),
			('Left',None),
			('Right',31),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|

room33 = dict([
            ('Name','Room 33'),
            ('Items',None),
			('Up',32),
			('Down',27),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room34 = dict([
            ('Name','Room 34'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',31),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room35 = dict([
            ('Name','Room 35'),
            ('Items',None),
			('Up',36),
			('Down',2),
			('Left',None),
			('Right',52),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room36 = dict([
            ('Name','Room 36'),
            ('Items',None),
			('Up',37),
			('Down',35),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room37 = dict([
            ('Name','Room 37'),
            ('Items',None),
			('Up',48),
			('Down',36),
			('Left',38),
			('Right',51),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room38 = dict([
            ('Name','Room 38'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',39),
			('Right',37),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room39 = dict([
            ('Name','Room 39'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',40),
			('Right',38),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room40 = dict([
            ('Name','Room 40'),
            ('Items',None),
			('Up',43),
			('Down',42),
			('Left',None),
			('Right',39),
            ('Doors',['Down',PurpleDoor]),
            ('NPC',None)
            ])

################################################################################|
room41 = dict([
            ('Name','Room 41'),
            ('Items','\033[0;33mOrange Key\033[00m'),
			('Up',None),
			('Down',None),
			('Left',None),
			('Right',6),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room42 = dict([
            ('Name','Room 42'),
            ('Items','\033[0;35mPurple gemstone\033[00m'),
			('Up',40),
			('Down',None),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room43 = dict([
            ('Name','Room 43'),
            ('Items',None),
			('Up',None),
			('Down',40),
			('Left',None),
			('Right',44),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room44 = dict([
            ('Name','Room 44'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',43),
			('Right',45),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room45 = dict([
            ('Name','Room 45'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',44),
			('Right',46),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room46 = dict([
            ('Name','Room 46'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',45),
			('Right',47),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room47 = dict([
            ('Name','Room 47'),
            ('Items',None),
			('Up',None),
			('Down',48),
			('Left',46),
			('Right',49),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room48 = dict([
            ('Name','Room 48'),
            ('Items',None),
			('Up',47),
			('Down',37),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room49 = dict([
            ('Name','Room 49'),
            ('Items',None),
			('Up',None),
			('Down',50),
			('Left',47),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room50 = dict([
            ('Name','Room 50'),
            ('Items',None),
			('Up',49),
			('Down',51),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room51 = dict([
            ('Name','Room 51'),
            ('Items',None),
			('Up',50),
			('Down',52),
			('Left',37),
			('Right',53),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room52 = dict([
            ('Name','Room 52'),
            ('Items',None),
			('Up',51),
			('Down',None),
			('Left',35),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room53 = dict([
            ('Name','Room 53'),
            ('Items',None),
			('Up',55),
			('Down',54),
			('Left',51),
			('Right',56),
            ('Doors',[None]),
            ('NPC',pdp)
            ])

################################################################################|
room54 = dict([
            ('Name','Room 54'),
            ('Items',None),
			('Up',53),
			('Down',None),
			('Left',None),
			('Right',57),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room55 = dict([
            ('Name','Room 55'),
            ('Items',None),
			('Up',None),
			('Down',53),
			('Left',None),
			('Right',83),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room56 = dict([
            ('Name','Room 56'),
            ('Items',None),
			('Up',None),
			('Down',57),
			('Left',53),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room57 = dict([
            ('Name','Room 57'),
            ('Items',None),
			('Up',56),
			('Down',58),
			('Left',54),
			('Right',68),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room58 = dict([
            ('Name','Room 58'),
            ('Items',None),
			('Up',57),
			('Down',62),
			('Left',60),
			('Right',64),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room59 = dict([
            ('Name','Room 59'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',None),
			('Right',60),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room60 = dict([
            ('Name','Room 60'),
            ('Items',None),
			('Up',None),
			('Down',61),
			('Left',59),
			('Right',58),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room61 = dict([
            ('Name','Room 61'),
            ('Items',None),
			('Up',60),
			('Down',63),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room62 = dict([
            ('Name','Room 62'),
            ('Items',None),
			('Up',58),
			('Down',None),
			('Left',63),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room63 = dict([
            ('Name','Room 63'),
            ('Items','\033[0;35mPurple Key\033[00m'),
			('Up',61),
			('Down',None),
			('Left',None),
			('Right',62),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room64 = dict([
            ('Name','Room 64'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',58),
			('Right',65),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room65 = dict([
            ('Name','Room 65'),
            ('Items',None),
			('Up',66),
			('Down',None),
			('Left',64),
			('Right',82),
            ('Doors',[None]),
            ('NPC',Wizard)
            ])

################################################################################|
room66 = dict([
            ('Name','Room 66'),
            ('Items',None),
			('Up',67),
			('Down',65),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room67 = dict([
            ('Name','Room 67'),
            ('Items',None),
			('Up',74),
			('Down',66),
			('Left',68),
			('Right',75),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room68 = dict([
            ('Name','Room 68'),
            ('Items',None),
			('Up',69),
			('Down',None),
			('Left',57),
			('Right',67),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room69 = dict([
            ('Name','Room 69'),
            ('Items',None),
			('Up',70),
			('Down',68),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room70 = dict([
            ('Name','Room 70'),
            ('Items',None),
			('Up',71),
			('Down',69),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room71 = dict([
            ('Name','Room 71'),
            ('Items',None),
			('Up',None),
			('Down',70),
			('Left',None),
			('Right',72),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room72 = dict([
            ('Name','Room 72'),
            ('Items',None),
			('Up',None),
			('Down',73),
			('Left',71),
			('Right',76),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room73 = dict([
            ('Name','Room 73'),
            ('Items',None),
			('Up',72),
			('Down',74),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room74 = dict([
            ('Name','Room 74'),
            ('Items',None),
			('Up',73),
			('Down',67),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room75 = dict([
            ('Name','Room 75'),
            ('Items',None),
			('Up',76),
			('Down',82),
			('Left',67),
			('Right',80),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room76 = dict([
            ('Name','Room 76'),
            ('Items',None),
			('Up',77),
			('Down',75),
			('Left',72),
			('Right',79),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room77 = dict([
            ('Name','Room 77'),
            ('Items',None),
			('Up',None),
			('Down',76),
			('Left',None),
			('Right',78),
            ('Doors',['Right',GreenDoor]),
            ('NPC',None)
            ])

################################################################################|
room78 = dict([
            ('Name','Room 78'),
            ('Items','\033[0;32mGreen Gemstone\033[00m'),
			('Up',None),
			('Down',None),
			('Left',77),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room79 = dict([
            ('Name','Room 79'),
            ('Items',None),
			('Up',None),
			('Down',None),
			('Left',76),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room80 = dict([
            ('Name','Room 80'),
            ('Items',None),
			('Up',None),
			('Down',81),
			('Left',75),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room81 = dict([
            ('Name','Room 81'),
            ('Items','\033[0;31mRed Key\033[00m'),
			('Up',80),
			('Down',None),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room82 = dict([
            ('Name','Room 82'),
            ('Items',None),
			('Up',75),
			('Down',None),
			('Left',65),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room83 = dict([
            ('Name','Room 83'),
            ('Items',None),
			('Up',84),
			('Down',None),
			('Left',55),
			('Right',None),
            ('Doors',['Up',OrangeDoor]),
            ('NPC',None)
            ])

################################################################################|
room84 = dict([
            ('Name','Room 84'),
            ('Items','\033[0;33mOrange gemstone\033[00m'),
			('Up',None),
			('Down',83),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|
room85 = dict([
            ('Name','Room 85'),
            ('Items',None),
			('Up',0),
			('Down',None),
			('Left',None),
			('Right',None),
            ('Doors',[None]),
            ('NPC',None)
            ])

################################################################################|LOCATIONS LIST
locations = [room0, room1, room2, room3, room4, room5, room6, room7, room8, room9, room10,
             room11, room12, room13, room14, room15, room16, room17, room18, room19, room20,
             room21, room22, room23, room24, room25, room26, room27, room28, room29, room30,
             room31, room32, room33, room34, room35, room36, room37, room38, room39, room40,
             room41, room42, room43, room44, room45, room46, room47, room48, room49, room50,
             room51, room52, room53, room54, room55, room56, room57, room58, room59, room60,
             room61, room62, room63, room64, room65, room66, room67, room68, room69, room70,
             room71, room72, room73, room74, room75, room76, room77, room78, room79, room80,
             room81, room82, room83, room84, room85]

################################################################################|PLAYER DICTIONARY
player = dict([
            ('Name',''),
            ('Inventory',[]),
            ('Room',0)
            ])

gems = ['\033[0;31mRed gemstone\033[00m', '\033[0;33mOrange gemstone\033[00m', '\033[0;33mYellow gemstone\033[00m', '\033[0;32mGreen Gemstone\033[00m','\033[0;34mBlue gemstone\033[00m', '\033[0;35mPurple gemstone\033[00m']
gemlocations = [room22, room84, room28, room78, room4, room42]
################################################################################|LOCATION,ITEMS,DIRECTION WHILE LOOP

WelcomeUser()

while True:
    if locations[player['Room']]['NPC'] != None:
        print('\033[0;33mYou have encountered %s!\033[00m'%locations[player['Room']]['NPC']['Name'])
        NPCtalk(locations[player['Room']]['NPC'])
        print('\033[0;33m%s\033[00m'%locations[player['Room']]['NPC']['YON'])
        answer = input('')
        if 'y' in answer.lower():
            locations[player['Room']]['NPC']['Yes']()
        else:
            TypeOut(locations[player['Room']]['NPC']['No'])

        locations[player['Room']]['NPC'] = None
        input('')
        os.system('cls')
        continue

    if locations[player['Room']]['Items'] != None:
        FindItem()

    print('You are in %s.'%locations[player['Room']]['Name'])

    if len(player['Inventory']) > 0:
        PrintInventory()

    if CanMakeRainbowKey():
        input('')
        os.system('cls')
        MakeRainbowKey()
        input('')
        continue



    PrintPossibleDirections()
    direction = input('Enter which direction: ') # U, D, L, R

    if direction.lower() == 'u' or 'up' in direction.lower():
        DirectionString = 'Up'

    elif direction.lower() == 'd' or 'down' in direction.lower():
        DirectionString = 'Down'

    elif direction.lower() == 'l' or 'left' in direction.lower():
        DirectionString = 'Left'

    elif direction.lower() == 'r' or 'right' in direction.lower():
        DirectionString = 'Right'

    elif 'chair' in direction.lower() and 'PewDiePie Chair' in player['Inventory']:
        print('\033[0;33mEnter the room number you wish to travel to:\n\033[00m')
        while True:
            try:
                travelto = int(input(''))
                if travelto in range(85):
                    break
                else:
                    os.system('cls')
                    continue
            except:
                os.system('cls')
                continue
        os.system('cls')
        print('\033[0;33mYou have now travelled to room %g using your \033[0;31mPewDiePie 100M Edition Clutch Chair\033[0;33m! ONLY $399.99!\033[00m'%travelto)
        player['Inventory'].remove('PewDiePie Chair')
        player['Room'] = travelto
        input('')
        os.system('cls')
        continue


    else:
        os.system('cls')
        continue


    if locations[player['Room']]['Doors'][0] == DirectionString and locations[player['Room']]['Doors'][1]['Requires'] not in player['Inventory']:
        print('\033[0;33mThere is a %s\033[0;33m in this direction, You need a %s\033[0;33m to unlock it...\033[37m'%(locations[player['Room']]['Doors'][1]['Name'],locations[player['Room']]['Doors'][1]['Requires']))
        input('')
        os.system('cls')
        continue

    elif locations[player['Room']]['Doors'][0] == DirectionString:
        print('\033[0;33mYou have unlocked the %s\033[0;33m...\033[37m'%locations[player['Room']]['Doors'][1]['Name'])
        player['Inventory'].remove(locations[player['Room']]['Doors'][1]['Requires'])
        locations[player['Room']]['Doors'] = [None]
        directionindex = locations[player['Room']][DirectionString]
        input('')

    else:
        directionindex = locations[player['Room']][DirectionString]

    if directionindex != None:
        player['Room'] = directionindex

    # Clears console
    os.system('cls')
