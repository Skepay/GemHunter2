# Program for automating the development of rooms.
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
    NPC = None # str

class RoomDisplay:
    def __init__(self, coords, roomNum):
        self.room = Room()
        self.room.name = roomNum
        self.rect = pygame.Rect(coords[0], coords[1], 20, 20)

    def drawRoom(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

        text = font.render('%g'%self.room.name, True, (0, 0, 0))
        screen.blit(text, (self.rect.x + 1, self.rect.y + 1))

    def drawLine(self, room2):
        pygame.draw.line(screen, (255, 255, 255), (self.rect.x + 10, self.rect.y + 10), (room2.rect.x + 10, room2.rect.y + 10))


rooms = [RoomDisplay((750, 400), 0)]

done = False
makingRoom = False

while not done:
    screen.fill((0, 0, 0))

    for room in rooms:
        room.drawRoom()

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if makingRoom:
                makingRoom = False

                # Calculating the distance from mouse cursor to room in both axes
                xDistance = abs(pos[0] - rooms[selectedRoomNum].rect.x)
                yDistance = abs(pos[1] - rooms[selectedRoomNum].rect.y)

                foundRoom = False
                for roomNum in range(len(rooms)):
                    if rooms[roomNum].rect.colliderect(newRoom):                        
                        foundRoom = True

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


    pygame.display.update()
