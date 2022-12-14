from time import sleep


def smiletimes0content(player):
    print("")
    print("     We haven't partied in so long, ", end="")
    sleep(2)
    print("it's about time we had some real, like, ", end="")
    sleep(2)
    print("with people fun.")
    sleep(1)
    print("     And I am ready.", end="")
    sleep(1)
    print(" to.", end="")
    sleep(1)
    print(" party.")
    sleep(1)
    print("")
    print("They open up this huge fan. ", end="")
    sleep(2)
    print("Like a hand fan. ", end="")
    sleep(2)
    print("Makes a loud ass noise.")
    sleep(2)

    print("It's the signature Smile Ambassador Party Fan (TM).")
    sleep(2)
    print("You and your partner laugh. ", end="")
    sleep(2)
    print("You're ready to get this party started.")
    print("")
    player.NPCs["smile"].times_talked = 1
    return True
