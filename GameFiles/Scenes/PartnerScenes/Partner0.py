# gives you ask for and use K.
from time import sleep


def partnertimes0content(player):
    print("who tells you")
    sleep(1)
    print("")
    print("     Babe, we can do the k if you want, just let me know when.")
    sleep(1)
    print("     I only have a little bit though.")
    sleep(1)
    if player.location == player.rooms["bathroom"]:
        print("     We could do it now if you want.")
    elif player.location != player.rooms["bathroom"]:
        print("     We'd have to go to the bathroom first of course.")
    player.memories.append("Ask for K")
    player.NPCs["partner"].times_talked = 1
    return False
