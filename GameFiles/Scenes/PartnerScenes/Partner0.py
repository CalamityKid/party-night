# gives you ask for and use K.
from time import sleep


def partnertimes0content(player):
    print("who tells you")
    sleep(1)
    print("")
    print("     Babe, ", end="")
    sleep(1)
    print("we can do the k if you want, ", end="")
    sleep(2)
    print("you just let me know when you want some.")
    sleep(2)
    print("     I only have a little bit though.")
    sleep(2)
    if player.location == player.rooms["bathroom"]:
        print("     We could do it now if you want.")
    elif player.location != player.rooms["bathroom"]:
        print("     We'd have to go to the bathroom first of course.")

    sleep(2)
    print("")
    print("You'll keep that in mind.")
    player.memories.append("Ask for K")
    player.NPCs["partner"].times_talked = 1
    return False
