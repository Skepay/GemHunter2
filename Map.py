class Room:
	def __init__(self, name, item, door, up, down, left, right, npc):
		self.name = name
		self.item = item
		self.door = door
		self.up = up
		self.down = down
		self.left = left
		self.right = right
		self.npc = npc

rooms = []

rooms.append(Room(0, None, None, 3, 4, 1, 2, None))                       # Room 0
rooms.append(Room(1, None, None, None, None, None, 0, 'BigDikMan'))       # Room 1
rooms.append(Room(2, None, None, None, None, 0, 5, 'PewDiePie'))          # Room 2
rooms.append(Room(3, None, None, None, 0, None, None, 'Wandering Traveler'))# Room 3
rooms.append(Room(4, None, None, 0, None, 6, 7, 'Elon Musk'))             # Room 4
rooms.append(Room(5, None, None, None, None, 2, None, None))              # Room 5
rooms.append(Room(6, None, None, None, 8, None, 4, 'TypeRace'))           # Room 6
rooms.append(Room(7, None, None, None, 10, 4, None, 'DrSnafu'))           # Room 7
rooms.append(Room(8, None, None, 6, None, None, 9, None))                 # Room 8
rooms.append(Room(9, None, None, None, None, 8, 10, None))                # Room 9
rooms.append(Room(10, None, None, 7, None, 9, None, None))                # Room 10