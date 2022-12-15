from ...Input import yesorno
from time import sleep


def partnergather0content(player):

    if "Gathering" in player.memories or "Not Gathering" in player.memories:
        return player.partnerscenes["Gather1"].run_scene(player)

    print("and complain about the music")
    sleep(1)
    print("it's killing you")
    print("")
    sleep(2)
    print("     The music is te ", end="")
    sleep(1)
    print("rri ", end="")
    sleep(1)
    print("ble.")
    sleep(1)
    print("     I could dance to a car alarm right now")
    sleep(2)
    print("     But this?")
    print("")
    sleep(2)
    print("you both grimace")
    sleep(2)
    print("but then your partner's face lights up")
    sleep(2)
    print("and half smirking starts saying")
    print("")
    sleep(2)
    print("     Remember that party in the warehouse?")
    print("     with the redhead in the crazy green jacket?")
    print("        Do you remember? (y/n)", end=" ")
    option = yesorno()
    print("")

    if option == True:
        print("you totally remember, that was a crazy jacket")

    elif option == False:

        print("you don't remember at all but you nod anyway")

    sleep(2)
    print("")
    print("     Yeah yeah! It's the same DJ.")
    sleep(2)
    print("     Jacket redhead was totally in control of the music that night.")
    print("")
    sleep(2)
    print("you start to get the idea")
    sleep(1)
    print("you get your friends down to the dance floor")
    sleep(2)
    print("you get enough attention and the DJ will listen probably")
    sleep(2)
    print("it's a good plan. ")
    sleep(2)
    print("     Do you wanna try? (y/n)", end=" ")
    option = yesorno()
    print("")

    if option == True:
        print("you say yeah, time to get your friends on the dance floor")
        player.memories.append("Gathering")
        player.memories.append("Plotting")
        return True

    elif option == False:
        print("you say no, too much effort")
        player.memories.append("Not Gathering")
        return True
