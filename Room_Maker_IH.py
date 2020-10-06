import pickle,pygame
pygame.init()

#screen = pygame.display.set_mode((2000,1200))
screen = pygame.display.set_mode((800,600))

font = pygame.font.Font('freesansbold.ttf',20)


def DrawRoom(x,y,num): # draws the white squares
    pygame.draw.rect(screen,(255,255,255),(x,y,40,40))

    sotext = font.render('%g'%num,True,(0,0,0))
    screen.blit(sotext,(x,y))


def DrawLine(x1,y1,x2,y2): # draws the line that connects the squares
    pygame.draw.line(screen,(255,255,255),(x1+20,y1+20),(x2+20,y2+20))


class Room:
    name = 'Room #'
    item = None
    up = None
    down = None
    left = None
    right = None
    NPC = None
    
    
Rooms = [Room()]
Rooms[0].name = 'Room 0'
#RoomCoords = [(1000,600)]
RoomCoords = [(400,300)]

MakingRoom = False
Quit = False

while True:
    screen.fill((0,0,0))

    pos = pygame.mouse.get_pos() # Getting mouse coordinates

    for event in pygame.event.get(): # exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

            
        if event.type == pygame.MOUSEBUTTONDOWN: # if click
            if event.button == 1:
                if MakingRoom: #If mouse is pressed while MakingRoom is equal to True
                    MakingRoom = False
                    Breakhere = False

                    #Calculating which axis is closer to mouse
                    Xdistance = abs(pos[0] - RoomCoords[Connectedto][0])
                    Ydistance = abs(pos[1] - RoomCoords[Connectedto][1])


                    for i in range(len(RoomCoords)): #Checking which room (if any) the user pressed
                        if pos[0] in range(RoomCoords[i][0],RoomCoords[i][0]+41) and pos[1] in range(RoomCoords[i][1], RoomCoords[i][1]+41):
                            if i != Connectedto:                        
                                if Xdistance > Ydistance:
                                    if RoomCoords[i][0] > RoomCoords[Connectedto][0]: #RIGHT
                                        Rooms[Connectedto].right = len(Rooms) - 1
                                        Rooms[-1].left = Connectedto
                                    else: #LEFT
                                        Rooms[Connectedto].left = len(Rooms) - 1
                                        Rooms[-1].right = Connectedto
                                else:
                                    if RoomCoords[i][1] > RoomCoords[Connectedto][1]: #DOWN
                                        Rooms[Connectedto].down = len(Rooms) - 1
                                        Rooms[-1].up = Connectedto
                                    else: #UP
                                        Rooms[Connectedto].up = len(Rooms) - 1
                                        Rooms[-1].down = Connectedto

                            Breakhere = True

                    if Breakhere:
                        break

                                    
                    Rooms.append(Room())
                    Rooms[-1].name = 'Room %g'%(len(Rooms)-1)
        
                    if Xdistance > Ydistance:
                        RoomCoords.append((pos[0], RoomCoords[Connectedto][1]))

                        if RoomCoords[-1][0] > RoomCoords[Connectedto][0]:
                            Rooms[Connectedto].right = len(Rooms) - 1
                            Rooms[-1].left = Connectedto
                        else:
                            Rooms[Connectedto].left = len(Rooms) - 1
                            Rooms[-1].right = Connectedto
                    else:
                        RoomCoords.append((RoomCoords[Connectedto][0], pos[1]))

                        if RoomCoords[-1][1] > RoomCoords[Connectedto][1]:
                            Rooms[Connectedto].down = len(Rooms) - 1
                            Rooms[-1].up = Connectedto
                        else:
                            Rooms[Connectedto].down = len(Rooms) - 1
                            Rooms[-1].up = Connectedto
                    
                else: #If mouse is pressed while MakingRoom is equal to False
                    for i in range(len(RoomCoords)): #Checking which room (if any) the user pressed
                        if pos[0] in range(RoomCoords[i][0],RoomCoords[i][0]+41) and pos[1] in range(RoomCoords[i][1], RoomCoords[i][1]+41):
                            MakingRoom = True
                            Connectedto = i #Saving the pressed room index into a variable
                            break


            elif event.button != 1:
                print("Enter the names of your items/npcs, leave blank for None")
                roomItem = input("What is the name of the item do you want to add to %s?\n"%Rooms[-1].name)
                roomNPC = input("What is the name of the NPC you want to add to %s?\n"%Rooms[-1].name)

                if roomItem != '':
                    Rooms[-1].item = roomItem 
                else:
                    Rooms[-1].item = None
                
                if roomNPC != '':
                    Rooms[-1].NPC = roomNPC
                else:
                    Rooms[-1].NPC = None

        
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                Quit = True
                        

    if MakingRoom: #If making room, draw the room
        Xdistance = abs(pos[0] - RoomCoords[Connectedto][0])
        Ydistance = abs(pos[1] - RoomCoords[Connectedto][1])
        if Xdistance > Ydistance:
            DrawRoom(pos[0], RoomCoords[Connectedto][1],len(Rooms))
        else:
            DrawRoom(RoomCoords[Connectedto][0], pos[1],len(Rooms))
        
            
    for i in range(len(Rooms)):        
        if Rooms[i].up != None:
            DrawLine(RoomCoords[i][0],RoomCoords[i][1],RoomCoords[Rooms[i].up][0],RoomCoords[Rooms[i].up][1])
        if Rooms[i].left != None:
            DrawLine(RoomCoords[i][0],RoomCoords[i][1],RoomCoords[Rooms[i].left][0],RoomCoords[Rooms[i].left][1])

        DrawRoom(RoomCoords[i][0],RoomCoords[i][1],i)
    

    pygame.display.update()
    

    if Quit:
        break

with open("bin.dat", "wb") as f:  
    pickle.dump(Rooms, f)

"""
for obj in Rooms:
    print('NAME:',obj.name)
    print('ITEM:', obj.item)
    print('NPC:',obj.NPC)
    print('UP:',obj.up)
    print('DOWN:',obj.down)
    print('LEFT:',obj.left)
    print('RIGHT:',obj.right)
    print('\n')
""" 
print('\n\n\nSuccessfully loaded rooms into "bin.dat"')

pygame.image.save(screen, "Map.jpeg")
print('\nSuccessfully saved map image under "Map.jpeg"')

