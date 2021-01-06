"""Haunted Castle, a game by Spyros Dellas.

Coded in Oct 2016 while reading 'Learn Python the Hard Way'.
# In this game the player can't beat the ghost alone. He must forge
# an ally with the knight to get to the treasure.
"""

from sys import exit
from textwrap import dedent


def get_answer(words_list):
    """This function scans player's input.

    If input contains more than one of the keywords provided by words_list,
    it is considered ambiguous and player is requested to repeat.
    """

    while True:
        answer = raw_input("> ").lower()
        answer_words = answer.split(" ")
        counter = 0
        for word in answer_words:
            if word in words_list:
                counter += 1
                answer = word # Player's answer is changed to the matching word
            else:
                continue
        if counter == 1:
            break
        else:
            print "Can't understand what you're saying. Can you re-phrase?"

    return answer


def start():
    """This function is called upon game start.

    You can only enter the castle; if you try to leave or
    fight the ghost you die.
    """

    message = """
    At last! You've found the ancient castle you were looking for
    the last ten years. The rumours say that there is a treasure here
    waiting for someone to take it...
    You are at the castle gate; two lions are engraved in the stone wall
    above you. Now is the time to decide, enter and face your fears
    or leave?\n"""
    print dedent(message)

    choice = get_answer(["enter", "leave"])

    if choice == "enter":
        inside_castle()
    else:
        message = """
        You turn around to leave, but after a few steps a ghost
        suddenly appears and blocks your way. It says:
        \"You can enter my castle anytime, but you can never leave!\"
        What are you going to do?
        1. Turn around and enter the castle
        2. Fight the ghost
        3. Run away\n"""
        print dedent(message)
        choice = get_answer(["enter", "fight", "run", "leave"])

        if choice == "enter":
            inside_castle()
        elif choice == "fight":
            die("You fight with the ghost, but you loose and die... ")
        else:
            die("You try to leave, but the ghost catches and kills you... ")


def inside_castle():
    message = """
    You enter the castle and start to explore it. Fortunately it's not a big
    place. There are only two buildings inside, a small and a big one, each
    one with a door.
    Which building do you wish to enter?\n"""
    print dedent(message)
    choice = get_answer(["small", "big"])

    if choice == "small":
        knight_room()
    else:
        ghost_room()


def knight_room():
    message = """
    You enter the small building and you meet a knight sitting on a bench. He
    stares at you and says:
    \"It seems that I'm not the only leaving person in this damn castle
    anymore. I arrived two days ago looking for the ancient treasure, but
    the ghost won't let me take it or leave the castle. There's no water
    or food and will starve to death if we stay. Help me to kill
    the ghost and I'll split the treasure with you.\"
    What's your decision? Are you going to help the knight or kill him?\n"""
    print dedent(message)
    choice = get_answer(["help", "kill"])

    if choice == "help":
        print ("You shake hands with the knight and head towards the big "
        "building... ")
        ghost_room(True)
    else:
        die("You try to kill the knight, but he kills you first... ")


def ghost_room(company = False):
    message = """
    You enter the big building and walk towards the door in the other end.
    Suddenly a ghost appears and says:
    \"Leave now or die!\"
    What are you going to do? Leave the room or fight the ghost?\n"""
    print dedent(message)
    choice = get_answer(["leave", "fight"])

    if choice == "leave":
        print "You try to exit the room, but the ghost catches and kills you..."
        if company:
            print "The knight runs towards the other door, but he faces same fate. "
            die()
        else:
            die()
    elif company:
        print ("The knight helps you to kill the ghost and then open the "
        "door that leads to the treasure...")
        treasure_room()
    else:
        die("The ghost kills you... ")


def treasure_room():
    message = """
    You enter and at last you are in front of the ancient
    treasure! You can split the treasure as agreed with the knight or you
    can try to kill him and take all the treasure for yourself.
    What's your choice?\n"""
    print dedent(message)
    choice = get_answer(["split", "kill"])

    if choice == "split":
        message = """
        Good choice, you split the treasure with the knight and you both become
        wealthy men and friends! Your families will rule the land for years
        to come...\n"""
        print dedent(message)
        die()
    else:
        die("You try to kill the knight, but you loose and die... ")


def die(exit_message = ""):
    print exit_message, "\bSee you next time!\n"
    exit(0)


print "\n", __doc__, "\n"
start()
