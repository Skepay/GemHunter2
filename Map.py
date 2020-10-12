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
rooms.append(Room(1, 'Tunnel Card', None, None, None, None, 0, None))     # Room 1
rooms.append(Room(2, None, [5, 'Red Door', ['Red Key']], None, None, 0, 5, None))# Room 2
rooms.append(Room(3, 'Red Key', None, None, 0, None, None, None))         # Room 3
rooms.append(Room(4, None, None, 0, None, None, None, None))              # Room 4
rooms.append(Room(5, None, None, None, None, 2, None, None))              # Room 5