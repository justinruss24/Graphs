from room import Room
from player import Player
from world import World

from utils import Stack, Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# backtracking directions
backtrack_moves = { "n":"s", "s":"n", "e":"w", "w":"e" }
# keep track of directions node visited for backtracking
backtrack = []
rooms = {}

# initialize dict. and keep track of current room/exits
rooms[player.current_room.id] = player.current_room.get_exits()
print("ROOMS: ", rooms)

starting = player.current_room.id
exits = player.current_room.get_exits()

# variable to keep track of previous room
last_room = None

print("GRAPH", room_graph)
print("EXITS: ", exits)

'''
PLAN
-----------
while len of rooms dict is < the graph
    check if current room is in rooms
    add it and its exits
    grab reverse of last direction traveled so it can be removed from exit options of current room
when a room has no exit, backtrack
    pop last reverse direction traveled to to remove it from backtrack list and add to traversal path
    then move player in the reverse direction
pop first available exit direction to remove it from possible exits
add to traversal path and add to end of backtrack path list
then move towards direction of first available exit
if only one room left unvisited, store it as well as its exits in room dictionary to avoid error using pop on empty list
'''

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
