"""This module contains the classes for the rooms in the map.

It is a requirement of this exercise that each room is a separate class.
Furthermore, to keep things simple, this game is a re-implementation
of the 'Haunted Castle' game from exercise 36.
Coded in Nov 2017 while reading 'Learn Python the Hard Way'.
"""

from textwrap import dedent
from sys import exit

class Room(object):
    """Base class for all other rooms."""

    def get_answer(self, words_list):
        """This method scans player's input.

        If player's input contains more than one of the keywords provided by
        words_list, it is considered ambiguous and player is asked to re-phrase.
        If player's input is matched with exactly one word from words_list,
        then that word is returned.
        """
        while True:
            answer = raw_input("> ").lower()
            answer_words = answer.split(" ")
            counter = 0

            for word in answer_words:
                if word in words_list:
                    counter += 1
                    answer = word
                else:
                    continue

            if counter == 1:
                break
            else:
                print "Can't understand what you're saying. Can you re-phrase?"

        return answer


class CastleGate(Room):
    """This is the starting scene of the game.

    You can only enter the castle; if you try to leave or
    fight the ghost you die.
    """

    def __init__(self, message = ""):
        self.message = """
        At last! You've found the ancient castle you were looking for
        the last ten years. The rumours say that there is a treasure here
        waiting for someone to take it...
        You are at the castle gate; two lions are engraved in the stone wall
        above you. Now is the time to decide, enter and face your fears
        or leave?\n"""

    def play(self):
        print dedent(self.message)
        choice = self.get_answer(["enter", "leave"])

        if choice == "enter":
            return ("inside_castle", "")
        else:
            _message = """
            You turn around to leave, but after a few steps a ghost
            suddenly appears and blocks your way. It says:
            \"You can enter my castle anytime, but you can never leave!\"
            What are you going to do?
            1. Turn around and enter the castle
            2. Fight the ghost
            3. Run away\n"""
            print dedent (_message)
            choice = self.get_answer(["enter", "fight", "run", "leave"])

            if choice == "enter":
                return ("inside_castle", "")
            elif choice == "fight":
                return (
                "die", "You fight with the ghost, but you loose and die..."
                )
            else:
                return (
                "die", "You try to leave, but the ghost catches you..."
                )


class InsideCastle(Room):

    def __init__(self, message = ""):
        self.message =  """
        You enter the castle and start to explore it. Fortunately it's not a big
        place. There are only two buildings inside, a small and a big one, each
        one with a door.
        Which building do you wish to enter?\n"""

    def play(self):
        print dedent(self.message)
        choice = self.get_answer(["small", "big"])

        if choice == "small":
            return ("knight_room", "")
        else:
            return ("ghost_room", "")


class KnightRoom(Room):

    def __init__(self, message = ""):
        self.message = """
        You enter the small building and you meet a knight sitting on a bench.
        He stares at you and says:
        \"It seems that I'm not the only leaving person in this damn castle
        anymore. I arrived two days ago looking for the ancient treasure, but
        the ghost won't let me take it or leave the castle. There's no water
        or food and will starve to death if we stay. Help me to kill
        the ghost and I'll split the treasure with you.\"
        What's your decision? Are you going to help the knight or kill him?\n"""

    def play(self):
        print dedent(self.message)
        choice = self.get_answer(["help", "kill"])

        if choice == "help":
            print ("You shake hands with the knight and head towards the big "
            "building... ")
            return ("ghost_room", True)
        else:
            return (
            "die", "You try to kill the knight, but he kills you first..."
            )


class GhostRoom(Room):

    def __init__(self, message = ""):
        self.message = message
        self._message = """
        You enter the big building and walk towards the door in the other end.
        Suddenly a ghost appears and says:
        \"Leave now or die!\"
        What are you going to do? Leave the room or fight the ghost?\n"""

    def play(self):
        print dedent(self._message)
        choice = self.get_answer(["leave", "fight"])

        if choice == "leave":
            print "You try to exit the room, but the ghost kills you..."
            if self.message:
                print "The knight runs to the other door, but he faces same fate."
                return ("die", "")
            else:
                return ("die", "")
        elif self.message:
            print ("The knight helps you to kill the ghost and then open the "
            "door that leads to the treasure...")
            return ("treasure_room", "")
        else:
            return ("die", "The ghost kills you... ")


class TreasureRoom(Room):

    def __init__(self, message = ""):
        self.message = """
        You enter and at last you are in front of the ancient
        treasure! You can split the treasure as agreed with the knight or you
        can try to kill him and take all the treasure for yourself.
        What's your choice?\n"""

    def play(self):
        print dedent(self.message)
        choice = self.get_answer(["split", "kill"])

        if choice == "split":
            _message = """
            Good choice, you split the treasure with the knight and you both
            become wealthy men and friends! Your families will rule the land
            for years to come...\n"""
            print dedent (_message)
            return ("die", "")
        else:
            return (
            "die", "You try to kill the knight, but you loose and die..."
            )


class Die(Room):

    def __init__(self, message = ""):
        self.message = message

    def play(self):
        if self.message:
            print self.message
        else:
            print "\bSee you next time!\n"
        exit(0)


game_map = {
"castle_gate" : CastleGate,
"inside_castle" : InsideCastle,
"knight_room" : KnightRoom,
"ghost_room" : GhostRoom,
"treasure_room" : TreasureRoom,
"die" : Die
}
