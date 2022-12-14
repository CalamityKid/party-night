from time import sleep
from ...Input import yesorno


def leavepartycontent(player):
    print("You turn to your partner")
    sleep(2)
    print("and say you want to leave the party")
    sleep(2)
    print("")
    print("     Yeah? ", end="")
    sleep(1)
    print("If you really wanna go")
    sleep(2)
    print("     I guess I'll go with you too.")
    sleep(2)
    print("")
    print("    Are you sure you want to LEAVE the party?")
    sleep(2)
    print("    Doing so will end the night. (y/n) ", end="")
    option = yesorno()
    print("")
    if option == True:
        print("    You and your partner leave the party without turning back.")
        sleep(3)
        player.gameover = True
        return None
    elif option == False:
        print("You reconsider.")
        sleep(2)
        print("Maybe you'll stay a bit longer.")
        sleep(2)
        print("")
        print("     Alright love.")
        sleep(1)
        print("     You let me know if you change your mind.")
        sleep(2)
        print("You half nod and turn back to the party.")
        return None
