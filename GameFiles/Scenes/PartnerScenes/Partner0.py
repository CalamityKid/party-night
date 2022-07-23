# gives you ask for and use K.


def partnertimes0content(player):
    print("     Babe, we can do the k if you want, just let me know when.")
    print("     I only have a little bit though.")
    if player.location == player.rooms["bathroom"]:
        print("We could do it now if you want.")
    elif player.location != player.rooms["bathroom"]:
        print("We'd have to go to the bathroom first of course.")
    player.memories.append("Ask for k")
    player.NPCs["partner"].times_talked = 1
    return False
