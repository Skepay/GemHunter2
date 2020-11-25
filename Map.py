# This map had to be manually edited for an npc and two doors.
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

rooms.append(Room(0, None, None, 4, 3, 1, 2, None))                       # Room 0
rooms.append(Room(1, None, None, None, 136, 5, 0, None))                  # Room 1
rooms.append(Room(2, None, None, None, None, 0, 55, None))                # Room 2
rooms.append(Room(3, None, [153, 'Gemstone Door', ['Red Gem', 'Orange Gem', 'Yellow Gem', 'Green Gem', 'Blue Gem', 'Indigo Gem', 'Violet Gem']], 0, 153, None, None, None))# Room 3
rooms.append(Room(4, None, None, 34, 0, 57, 58, None))                    # Room 4
rooms.append(Room(5, None, None, 6, 8, 10, 1, None))                      # Room 5
rooms.append(Room(6, None, None, None, 5, 7, None, None))                 # Room 6
rooms.append(Room(7, None, None, 86, 197, 11, 6, None))                   # Room 7
rooms.append(Room(8, None, None, 5, None, 9, None, None))                 # Room 8
rooms.append(Room(9, None, None, 10, None, None, 8, None))                # Room 9
rooms.append(Room(10, None, None, None, 9, None, 5, None))                # Room 10
rooms.append(Room(11, None, None, None, 12, None, 7, None))               # Room 11
rooms.append(Room(12, None, None, 11, None, 13, None, None))              # Room 12
rooms.append(Room(13, None, None, None, None, 14, 12, None))              # Room 13
rooms.append(Room(14, None, None, 15, 19, 17, 13, None))                  # Room 14
rooms.append(Room(15, None, None, 118, 14, 115, 16, None))                # Room 15
rooms.append(Room(16, None, None, None, None, 15, None, None))            # Room 16
rooms.append(Room(17, None, None, None, None, 18, 14, None))              # Room 17
rooms.append(Room(18, None, None, None, None, 134, 17, None))             # Room 18
rooms.append(Room(19, None, None, 14, 24, 20, 22, None))                  # Room 19
rooms.append(Room(20, 'Green Key', None, None, None, 21, 19, None))       # Room 20
rooms.append(Room(21, None, None, None, None, None, 20, None))            # Room 21
rooms.append(Room(22, None, None, None, None, 19, 23, None))              # Room 22
rooms.append(Room(23, None, None, None, None, 22, None, None))            # Room 23
rooms.append(Room(24, None, None, 19, 29, 25, 27, None))                  # Room 24
rooms.append(Room(25, None, None, None, None, 26, 24, None))              # Room 25
rooms.append(Room(26, None, None, None, None, None, 25, None))            # Room 26
rooms.append(Room(27, None, None, None, None, 24, 28, None))              # Room 27
rooms.append(Room(28, None, None, None, None, 27, None, None))            # Room 28
rooms.append(Room(29, None, None, 24, 184, 32, 30, 'PewDiePie'))          # Room 29
rooms.append(Room(30, None, None, None, 185, 29, 31, None))               # Room 30
rooms.append(Room(31, None, None, None, 186, 30, None, None))             # Room 31
rooms.append(Room(32, None, None, None, 183, 33, 29, None))               # Room 32
rooms.append(Room(33, None, None, None, 99, None, 32, None))              # Room 33
rooms.append(Room(34, None, None, 74, 4, 35, 36, None))                   # Room 34
rooms.append(Room(35, None, None, 39, None, None, 34, None))              # Room 35
rooms.append(Room(36, None, None, 37, None, 34, 133, None))               # Room 36
rooms.append(Room(37, None, None, None, 36, None, 38, None))              # Room 37
rooms.append(Room(38, None, None, 46, None, 37, None, None))              # Room 38
rooms.append(Room(39, None, None, None, 35, 40, None, None))              # Room 39
rooms.append(Room(40, None, None, 41, 43, None, 39, None))                # Room 40
rooms.append(Room(41, None, None, 42, 40, None, None, None))              # Room 41
rooms.append(Room(42, None, None, None, 41, None, None, None))            # Room 42
rooms.append(Room(43, None, None, 40, 44, None, None, None))              # Room 43
rooms.append(Room(44, None, None, 43, 45, None, None, None))              # Room 44
rooms.append(Room(45, None, None, 44, None, None, None, None))            # Room 45
rooms.append(Room(46, None, None, 129, 38, None, 47, None))               # Room 46
rooms.append(Room(47, None, None, 130, None, 46, 48, 'Dr Snafu'))         # Room 47
rooms.append(Room(48, None, None, 188, 49, 47, 73, None))                 # Room 48
rooms.append(Room(49, None, None, 48, 68, None, 72, None))                # Room 49
rooms.append(Room(50, None, None, 72, 71, 68, None, None))                # Room 50
rooms.append(Room(51, None, None, None, None, 73, 52, None))              # Room 51
rooms.append(Room(52, None, None, 53, None, 51, None, None))              # Room 52
rooms.append(Room(53, None, [54, 'Red Door', ['Red Key']], None, 52, None, 54, None))# Room 53
rooms.append(Room(54, 'Red Gem', None, None, None, 53, None, None))       # Room 54
rooms.append(Room(55, None, None, None, None, 2, 56, None))               # Room 55
rooms.append(Room(56, None, None, None, 62, 55, 59, None))                # Room 56
rooms.append(Room(57, None, None, None, None, None, 4, None))             # Room 57
rooms.append(Room(58, None, None, None, None, 4, None, None))             # Room 58
rooms.append(Room(59, None, None, 60, 64, 56, 65, None))                  # Room 59
rooms.append(Room(60, None, [61, 'Violet Door', ['Violet Key']], None, 59, 61, None, None))# Room 60
rooms.append(Room(61, 'Violet Gem', None, None, None, None, 60, None))    # Room 61
rooms.append(Room(62, None, None, 56, None, 63, 64, None))                # Room 62
rooms.append(Room(63, None, None, None, 155, None, 62, None))             # Room 63
rooms.append(Room(64, None, None, 59, None, 62, None, None))              # Room 64
rooms.append(Room(65, None, None, 68, 66, 59, None, None))                # Room 65
rooms.append(Room(66, None, None, 65, None, None, 67, None))              # Room 66
rooms.append(Room(67, None, None, None, None, 66, 69, None))              # Room 67
rooms.append(Room(68, None, None, 49, 65, None, 50, None))                # Room 68
rooms.append(Room(69, 'Red Key', None, 70, None, 67, None, None))         # Room 69
rooms.append(Room(70, None, None, 122, 69, 71, None, None))               # Room 70
rooms.append(Room(71, None, None, 50, None, None, 70, None))              # Room 71
rooms.append(Room(72, None, None, 73, 50, 49, 112, None))                 # Room 72
rooms.append(Room(73, None, None, None, 72, 48, 51, None))                # Room 73
rooms.append(Room(74, None, None, None, 34, None, 75, None))              # Room 74
rooms.append(Room(75, None, None, 76, None, 74, None, None))              # Room 75
rooms.append(Room(76, None, None, None, 75, None, 77, None))              # Room 76
rooms.append(Room(77, None, None, 78, 196, 76, None, None))               # Room 77
rooms.append(Room(78, None, None, 131, 77, 79, None, None))               # Room 78
rooms.append(Room(79, None, None, 132, None, 80, 78, None))               # Room 79
rooms.append(Room(80, None, None, 81, None, None, 79, None))              # Room 80
rooms.append(Room(81, None, None, None, 80, 82, None, None))              # Room 81
rooms.append(Room(82, None, None, 181, 83, None, 81, None))               # Room 82
rooms.append(Room(83, None, None, 82, 84, None, None, None))              # Room 83
rooms.append(Room(84, None, None, 83, None, None, 85, None))              # Room 84
rooms.append(Room(85, None, [195, 'Yellow Door', ['Yellow Key']], None, 195, 84, None, None))# Room 85
rooms.append(Room(86, None, None, 90, 7, 87, 88, None))                   # Room 86
rooms.append(Room(87, None, None, 93, None, None, 86, 'Maya'))            # Room 87
rooms.append(Room(88, None, None, 89, None, 86, None, None))              # Room 88
rooms.append(Room(89, None, None, None, 88, 90, None, None))              # Room 89
rooms.append(Room(90, None, None, 91, 86, None, 89, None))                # Room 90
rooms.append(Room(91, None, None, None, 90, 93, 92, None))                # Room 91
rooms.append(Room(92, None, None, None, None, 91, 94, None))              # Room 92
rooms.append(Room(93, None, None, None, 87, None, 91, None))              # Room 93
rooms.append(Room(94, None, None, 95, None, 92, None, None))              # Room 94
rooms.append(Room(95, None, None, None, 94, 96, None, None))              # Room 95
rooms.append(Room(96, None, None, None, None, 97, 95, None))              # Room 96
rooms.append(Room(97, None, [98, 'Indigo Door', ['Indigo Key']], None, 98, None, 96, None))# Room 97
rooms.append(Room(98, 'Indigo Gem', None, 97, None, None, None, None))    # Room 98
rooms.append(Room(99, None, None, 33, None, 111, 100, None))              # Room 99
rooms.append(Room(100, None, None, None, None, 99, 101, None))            # Room 100
rooms.append(Room(101, None, None, None, None, 100, 102, None))           # Room 101
rooms.append(Room(102, None, None, None, None, 101, 103, None))           # Room 102
rooms.append(Room(103, None, None, None, 104, 102, None, None))           # Room 103
rooms.append(Room(104, None, None, 103, 177, 105, None, None))            # Room 104
rooms.append(Room(105, None, None, None, None, 106, 104, None))           # Room 105
rooms.append(Room(106, 'Violet Key', None, None, 179, 107, 105, None))    # Room 106
rooms.append(Room(107, None, None, None, 180, 108, 106, None))            # Room 107
rooms.append(Room(108, None, None, None, 109, None, 107, None))           # Room 108
rooms.append(Room(109, None, None, 108, None, 110, None, None))           # Room 109
rooms.append(Room(110, None, None, 111, None, None, 109, None))           # Room 110
rooms.append(Room(111, None, None, None, 110, None, 99, None))            # Room 111
rooms.append(Room(112, None, None, None, None, 72, 113, None))            # Room 112
rooms.append(Room(113, None, None, None, 114, 112, None, None))           # Room 113
rooms.append(Room(114, None, None, 113, None, None, None, None))          # Room 114
rooms.append(Room(115, None, None, 116, 120, None, 15, None))             # Room 115
rooms.append(Room(116, None, None, None, 115, 117, None, None))           # Room 116
rooms.append(Room(117, None, None, None, None, None, 116, None))          # Room 117
rooms.append(Room(118, None, None, None, 15, 119, None, None))            # Room 118
rooms.append(Room(119, None, None, None, None, None, 118, None))          # Room 119
rooms.append(Room(120, None, None, 115, None, None, 121, None))           # Room 120
rooms.append(Room(121, None, None, None, None, 120, None, None))          # Room 121
rooms.append(Room(122, None, None, None, 70, None, 123, None))            # Room 122
rooms.append(Room(123, None, None, None, 124, 122, None, None))           # Room 123
rooms.append(Room(124, None, None, 123, None, None, 125, None))           # Room 124
rooms.append(Room(125, None, None, 126, None, 124, None, None))           # Room 125
rooms.append(Room(126, None, None, None, 125, 127, None, None))           # Room 126
rooms.append(Room(127, None, [128, 'Orange Door', ['Orange Key']], None, 128, None, 126, None))# Room 127
rooms.append(Room(128, 'Orange Gem', None, 127, None, None, None, None))  # Room 128
rooms.append(Room(129, None, None, None, 46, None, 130, None))            # Room 129
rooms.append(Room(130, None, None, None, 47, 129, None, None))            # Room 130
rooms.append(Room(131, None, None, None, 78, 132, None, None))            # Room 131
rooms.append(Room(132, None, None, 182, 79, None, 131, None))             # Room 132
rooms.append(Room(133, None, None, None, None, 36, None, None))           # Room 133
rooms.append(Room(134, None, [135, 'Green Door', ['Green Key']], 135, None, None, 18, None))# Room 134
rooms.append(Room(135, 'Green Gem', None, None, 134, None, None, None))   # Room 135
rooms.append(Room(136, None, None, 1, 137, None, None, None))             # Room 136
rooms.append(Room(137, None, None, 136, 148, 138, None, None))            # Room 137
rooms.append(Room(138, None, None, None, 139, 141, 137, None))            # Room 138
rooms.append(Room(139, None, None, 138, None, 140, None, None))           # Room 139
rooms.append(Room(140, None, None, 141, None, None, 139, None))           # Room 140
rooms.append(Room(141, None, None, None, 140, 142, 138, None))            # Room 141
rooms.append(Room(142, 'Yellow Key', None, None, 143, None, 141, None))   # Room 142
rooms.append(Room(143, None, None, 142, 144, None, None, None))           # Room 143
rooms.append(Room(144, None, None, 143, 149, None, 145, None))            # Room 144
rooms.append(Room(145, None, None, None, None, 144, 146, None))           # Room 145
rooms.append(Room(146, None, None, None, 150, 145, 147, 'Elon Musk'))     # Room 146
rooms.append(Room(147, None, None, 148, None, 146, 171, None))            # Room 147
rooms.append(Room(148, None, None, 137, 147, None, None, None))           # Room 148
rooms.append(Room(149, None, None, 144, 151, None, None, None))           # Room 149
rooms.append(Room(150, None, None, 146, 154, None, None, None))           # Room 150
rooms.append(Room(151, None, [152, 'Blue Door', ['Blue Key']], 149, 152, None, None, None))# Room 151
rooms.append(Room(152, 'Blue Gem', None, 151, None, None, None, None))    # Room 152
rooms.append(Room(153, 'Exit Door', None, 3, None, None, None, None))            # Room 153
rooms.append(Room(154, None, None, 150, None, None, None, None))          # Room 154
rooms.append(Room(155, None, None, 63, None, None, 156, None))            # Room 155
rooms.append(Room(156, None, None, None, None, 155, 157, None))           # Room 156
rooms.append(Room(157, None, None, None, 158, 156, 164, None))            # Room 157
rooms.append(Room(158, None, None, 157, None, 159, 160, None))            # Room 158
rooms.append(Room(159, None, None, None, 161, 165, 158, None))            # Room 159
rooms.append(Room(160, None, None, 164, 163, 158, None, None))            # Room 160
rooms.append(Room(161, None, None, 159, None, None, 162, None))           # Room 161
rooms.append(Room(162, None, None, None, None, 161, 163, 'Walter White')) # Room 162
rooms.append(Room(163, None, None, 160, None, 162, None, None))           # Room 163
rooms.append(Room(164, None, None, None, 160, 157, None, None))           # Room 164
rooms.append(Room(165, None, None, None, 166, None, 159, None))           # Room 165
rooms.append(Room(166, None, None, 165, None, 167, None, None))           # Room 166
rooms.append(Room(167, None, None, 168, 170, None, 166, None))            # Room 167
rooms.append(Room(168, None, None, 169, 167, None, None, None))           # Room 168
rooms.append(Room(169, None, None, None, 168, None, None, None))          # Room 169
rooms.append(Room(170, None, None, 167, 171, None, None, None))           # Room 170
rooms.append(Room(171, None, None, 170, 172, 147, None, None))            # Room 171
rooms.append(Room(172, None, None, 171, 173, None, None, None))           # Room 172
rooms.append(Room(173, None, None, 172, 174, None, None, None))           # Room 173
rooms.append(Room(174, None, None, 173, 175, None, None, None))           # Room 174
rooms.append(Room(175, None, None, 174, None, 176, None, None))           # Room 175
rooms.append(Room(176, None, None, None, None, None, 175, 'Computer'))    # Room 176
rooms.append(Room(177, None, None, 104, None, 178, None, None))           # Room 177
rooms.append(Room(178, None, None, None, None, 179, 177, None))           # Room 178
rooms.append(Room(179, None, None, 106, None, 180, 178, None))            # Room 179
rooms.append(Room(180, None, None, 107, None, None, 179, None))           # Room 180
rooms.append(Room(181, None, None, None, 82, None, 182, 'BigDikman'))     # Room 181
rooms.append(Room(182, None, None, None, 132, 181, None, None))           # Room 182
rooms.append(Room(183, None, None, 32, None, None, 184, None))            # Room 183
rooms.append(Room(184, None, None, 29, None, 183, None, None))            # Room 184
rooms.append(Room(185, None, None, 30, 187, None, None, None))            # Room 185
rooms.append(Room(186, 'Blue Key', None, 31, None, None, None, None))     # Room 186
rooms.append(Room(187, None, None, 185, None, None, None, None))          # Room 187
rooms.append(Room(188, None, None, 191, 48, 190, 189, None))              # Room 188
rooms.append(Room(189, None, None, None, None, 188, None, None))          # Room 189
rooms.append(Room(190, None, None, None, None, None, 188, None))          # Room 190
rooms.append(Room(191, None, None, None, 188, 192, None, None))           # Room 191
rooms.append(Room(192, None, None, None, None, 193, 191, None))           # Room 192
rooms.append(Room(193, None, None, 194, None, None, 192, None))           # Room 193
rooms.append(Room(194, None, None, None, 193, None, None, 'Wandering Traveler'))          # Room 194
rooms.append(Room(195, 'Yellow Gem', None, 85, None, None, None, None))   # Room 195
rooms.append(Room(196, 'Orange Key', None, 77, None, None, None, None))   # Room 196
rooms.append(Room(197, None, None, 7, None, None, 198, None))             # Room 197
rooms.append(Room(198, None, None, None, 199, 197, None, None))           # Room 198
rooms.append(Room(199, 'Indigo Key', None, 198, None, None, None, None))  # Room 199