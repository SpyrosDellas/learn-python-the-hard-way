"""Haunted Castle, a game by Spyros Dellas.

Coded in Nov 2016 while reading 'Learn Python the Hard Way'.
Description: In this game the player can't beat the ghost alone. He must forge
an ally with the knight to get to the treasure.
"""

from . import gmp

class Engine(object):
    """This is the game engine."""

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def play(self):
        """This method receives the returned tuple from each room and
        calls the next one.

        The first element of the tuple is a string corresponding to the next
        room and the second is a string containing a message to initialize the
        room (always an empty string, except for GhostRoom).
        """
        next_scene = self.start_scene
        while True:
            room, message = next_scene.play()
            next_scene = gmp.game_map[room](message)

#print __doc__, "\n"

#start_scene = gmp.game_map["castle_gate"]()
#game_engine = Engine(start_scene)
#game_engine.play()
