# Program for automating the development of rooms.
import os
import pickle #rick lol haha
import pygame
pygame.init()

screen = pygame.display.set_mode((1500, 800))
font = pygame.font.Font('freesansbold.ttf',10)

class Room: # stores attributes of each room
    name = None # int
    item = None # str
    door = None # int
    up = None   # room
    down = None # room
    left = None # room
    right = None # room
    npc = None # str

class RoomDisplay:
    def __init__(self, coords, roomNum):
        self.room = Room()
        self.room.name = roomNum
        self.rect = pygame.Rect(coords[0], coords[1], 20, 20)

    def drawRoom(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

        text = font.render('%g'%self.room.name, True, (0, 0, 0))
        screen.blit(text, (self.rect.x + 1, self.rect.y + 1))

        if self.room.door != None:
            pygame.draw.rect(screen, (102, 51, 0), (self.rect.x + 1, self.rect.y + 15, 4, 4))
        if self.room.item != None:
            pygame.draw.rect(screen, (0, 0, 153), (self.rect.x + 8, self.rect.y + 15, 4, 4))
        if self.room.npc != None:
            pygame.draw.rect(screen, (153, 0, 153), (self.rect.x + 15, self.rect.y + 15, 4, 4))

    def drawLine(self, room2):
        pygame.draw.line(screen, (255, 255, 255), (self.rect.x + 10, self.rect.y + 10), (room2.rect.x + 10, room2.rect.y + 10))


fileName = input('Enter name of map file (leave blank for new map): ')
if fileName != '':
    inFile = open(fileName + '_RM_DATA.dat', 'rb')
    inFile.seek(0)
    rooms = pickle.load(inFile)
else:
    rooms = [RoomDisplay((750, 400), 0)]

done = False
makingRoom = False

while not done:
    screen.fill((0, 0, 0))

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if makingRoom:
                makingRoom = False

                # Calculating the distance from mouse cursor to room in both axes
                xDistance = abs(pos[0] - rooms[selectedRoomNum].rect.x)
                yDistance = abs(pos[1] - rooms[selectedRoomNum].rect.y)

                foundRoom = False
                for roomNum in range(len(rooms)):
                    if rooms[roomNum].rect.colliderect(newRoom):                        
                        foundRoom = True

                        if roomNum == selectedRoomNum:
                            break

                        if xDistance > yDistance: # If room is being added on the X axis
                            if rooms[roomNum].rect.x > rooms[selectedRoomNum].rect.x: # If room pressed is to the right
                                rooms[roomNum].room.left = selectedRoomNum
                                rooms[selectedRoomNum].room.right = roomNum       
                            else: # If room pressed is to the left
                                rooms[roomNum].room.right = selectedRoomNum
                                rooms[selectedRoomNum].room.left = roomNum  
                        else: # If room is being added on the Y axis
                            if rooms[roomNum].rect.y > rooms[selectedRoomNum].rect.y: # If room pressed is down
                                rooms[roomNum].room.up = selectedRoomNum
                                rooms[selectedRoomNum].room.down = roomNum       
                            else: # If room pressed is up
                                rooms[roomNum].room.down = selectedRoomNum
                                rooms[selectedRoomNum].room.up = roomNum  
                        break


                if not foundRoom:
                    if xDistance > yDistance:
                        rooms.append(RoomDisplay((pos[0] - 10, rooms[selectedRoomNum].rect.y), len(rooms)))
                        if rooms[-1].rect.x > rooms[selectedRoomNum].rect.x: # If room is being added to the right
                            rooms[selectedRoomNum].room.right = len(rooms) - 1
                            rooms[-1].room.left = selectedRoomNum
                        else: # If room is being added to the left
                            rooms[selectedRoomNum].room.left = len(rooms) - 1
                            rooms[-1].room.right = selectedRoomNum
                    else:
                        rooms.append(RoomDisplay((rooms[selectedRoomNum].rect.x, pos[1] - 10), len(rooms)))
                        if rooms[-1].rect.y > rooms[selectedRoomNum].rect.y: # If room is being added down
                            rooms[selectedRoomNum].room.down = len(rooms) - 1
                            rooms[-1].room.up = selectedRoomNum
                        else: # If room is being added up
                            rooms[selectedRoomNum].room.up = len(rooms) - 1
                            rooms[-1].room.down = selectedRoomNum                   


            else:
                for roomNum in range(len(rooms)):
                    if rooms[roomNum].rect.collidepoint(pos):
                        selectedRoomNum = roomNum
                        makingRoom = True
                        break

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            makingRoom = False
            
            foundRoom = False
            for roomNum in range(len(rooms)):
                if rooms[roomNum].rect.collidepoint(pos):
                    selectedRoomNum = roomNum
                    foundRoom = True
                    break
            
            if not foundRoom or rooms[selectedRoomNum].room.name == 0:
                break


            if rooms[-1].room.left != None:
                rooms[rooms[-1].room.left].room.right = selectedRoomNum
            if rooms[-1].room.right != None:
                rooms[rooms[-1].room.right].room.left = selectedRoomNum
            if rooms[-1].room.up != None:
                rooms[rooms[-1].room.up].room.down = selectedRoomNum
            if rooms[-1].room.down != None:
                rooms[rooms[-1].room.down].room.up = selectedRoomNum

            if rooms[selectedRoomNum].room.left != None:
                rooms[rooms[selectedRoomNum].room.left].room.right = None
            if rooms[selectedRoomNum].room.right != None:
                rooms[rooms[selectedRoomNum].room.right].room.left = None
            if rooms[selectedRoomNum].room.up != None:
                rooms[rooms[selectedRoomNum].room.up].room.down = None
            if rooms[selectedRoomNum].room.down != None:
                rooms[rooms[selectedRoomNum].room.down].room.up = None
            
            rooms[-1].room.name = selectedRoomNum
            rooms[selectedRoomNum] = rooms[-1]
            del rooms[-1]

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            foundRoom = False
            for roomNum in range(len(rooms)):
                if rooms[roomNum].rect.collidepoint(pos):
                    selectedRoomNum = roomNum
                    foundRoom = True
                    break
            
            if not foundRoom:
                break
            
            os.system('cls')
            print('Current settings for room %g:'%rooms[selectedRoomNum].room.name)
            print('Door =', rooms[selectedRoomNum].room.door)
            print('Item =', rooms[selectedRoomNum].room.item)
            print('NPC  =', rooms[selectedRoomNum].room.npc)
            print('*' * 35)

            print('Change settings for room %g:'%rooms[selectedRoomNum].room.name)

            door = input('Door = ')
            if door != '':
                try:
                    rooms[selectedRoomNum].room.door = int(door)
                except:
                    rooms[selectedRoomNum].room.door = None
            else:
                rooms[selectedRoomNum].room.door = None

            item = input('Item = ')
            if item != '':
                rooms[selectedRoomNum].room.item = item
            else:
                rooms[selectedRoomNum].room.item = None

            npc = input('NPC  = ')
            if npc != '':
                rooms[selectedRoomNum].room.npc = npc
            else:
                rooms[selectedRoomNum].room.npc = None

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                done = True
            
            

    
    if makingRoom:
        xDistance = abs(pos[0] - rooms[selectedRoomNum].rect.x)
        yDistance = abs(pos[1] - rooms[selectedRoomNum].rect.y)

        if xDistance > yDistance:
            newRoom = RoomDisplay((pos[0] - 10, rooms[selectedRoomNum].rect.y), len(rooms))
        else:
            newRoom = RoomDisplay((rooms[selectedRoomNum].rect.x, pos[1] - 10), len(rooms))

        drawNewRoom = True
        for room in rooms:
            if room.rect.colliderect(newRoom):
                drawNewRoom = False
                room.drawLine(rooms[selectedRoomNum])
                break

        if drawNewRoom:
            newRoom.drawLine(rooms[selectedRoomNum])
            newRoom.drawRoom()


    for room in rooms:
        if room.room.up != None:
            room.drawLine(rooms[room.room.up])
        if room.room.left != None:
            room.drawLine(rooms[room.room.left])

        room.drawRoom()


    pygame.display.update()


# MAP IS FINISHED AT THIS POINT
# SAVING ALL NECESSARY FILES

fileName = input('Enter file name for map files: ')

pygame.image.save(screen, fileName + '.png')    # Saving png of map
print('Saved image of map under name %s.png'%fileName)

with open(fileName + '_RM_DATA.dat', 'wb') as outFile: # Saving to room_maker data file
    pickle.dump(rooms, outFile)
print('Saved room maker map data under name %s_RM_DATA.dat'%fileName)

for i in range(len(rooms)):
    rooms[i] = rooms[i].room

with open(fileName + '.dat', 'wb') as outFile:  # Saving to game data file
    pickle.dump(rooms, outFile)
print('Saved game map data under name %s.dat'%fileName)
