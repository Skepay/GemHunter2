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

rooms.append(Room(0, None, None, 3, 2, 1, 4, None))                       # Room 0
rooms.append(Room(1, 'Red Key', None, None, None, None, 0, None))         # Room 1
rooms.append(Room(2, None, None, 0, None, None, None, 'Elon Musk'))       # Room 2
rooms.append(Room(3, None, None, None, 0, None, None, 'PewDiePie'))       # Room 3
rooms.append(Room(4, None, [5, 'Red Door', ['Red Key']], None, None, 0, 5, None))# Room 4
rooms.append(Room(5, None, None, None, None, 4, None, 'Maya'))            # Room 5