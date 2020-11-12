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

rooms.append(Room(0, None, None, 4, 5, 1, 3, None))                       # Room 0
rooms.append(Room(1, None, None, None, None, 2, 0, 'Walter White'))                 # Room 1
rooms.append(Room(2, None, None, None, None, None, 1, None))              # Room 2
rooms.append(Room(3, None, None, None, None, 0, None, None))              # Room 3
rooms.append(Room(4, 'Water', None, None, 0, 8, 9, None))                 # Room 4
rooms.append(Room(5, None, None, 0, None, 6, 7, None))                    # Room 5
rooms.append(Room(6, None, None, None, None, None, 5, 'Dr Snafu'))        # Room 6
rooms.append(Room(7, None, None, None, None, 5, None, 'Wandering Traveler'))# Room 7
rooms.append(Room(8, None, None, None, None, None, 4, 'Computer'))        # Room 8
rooms.append(Room(9, None, None, None, None, 4, None, None))              # Room 9