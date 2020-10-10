# Program for automating the development of rooms.


<<<<<<< HEAD

=======
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
    def __init__(self, coords):
        self.room = Room()
        self.coords = coords

    def drawRoom(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.coords[0], self.coords[1], 20, 20))

        text = font.render('%g'%self.room.name, True, (0, 0, 0))
        screen.blit(text, (self.coords[0], self.coords[1]))

    def DrawLine(self, room2):
        pygame.draw.line(screen, (255, 255, 255), (self.coords[0] + 10, self.coords[1] + 20), (room2.coords[0] + 20, room2.coords[1] + 20))



rooms = [Room()]
Rooms[0] = 0
>>>>>>> d91737d730b1047621c16b512f31c3f0f658da9a
