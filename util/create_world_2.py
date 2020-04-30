from django.contrib.auth.models import User
from adventure.models import Player, Room
from faker import Faker
import random

Room.objects.all().truncate()
my_fake = Faker()

my_rooms = []

for i in range(200):
  my_rooms.append(Room(title=my_fake.misc(), description=my_fake.paragraph()))


for i in range(1, 1000):
  
  # random direction
  value = random.randint(1, 4)
  
  # random room 1
  x = random.randint(0, 200)
  

  # north
  if value == 1:
    # previous_room.connect_rooms(room, room_direction)
    my_rooms[x].connect_rooms(my_rooms[x - 1], 'n')
    my_rooms[x - 1].connect_rooms(x, 's')

  # south
  elif value == 2:
    my_rooms[x].connect_rooms(my_rooms[x + 1], 's')
    my_rooms[x + 1].connect_rooms(x, 'n')

  # east
  elif value == 3:
    my_rooms[x].connect_rooms(my_rooms[x + 2], 'e')
    my_rooms[x + 2].connect_rooms(x, 'w')
  
  # west
  elif value == 3:
    my_rooms[x].connect_rooms(my_rooms[x + 3], 'w')
    my_rooms[x + 3].connect_rooms(x, 'e')


  

r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

