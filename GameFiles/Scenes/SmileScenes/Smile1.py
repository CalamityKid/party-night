from ...Input import yesorno
from time import sleep

##########################################SMILE SCENES
######################Smile Times1, offers G


def smiletimes1content(player):
    if player.location == player.rooms["bathroom"]:
        print("")
        print("The smile ambassador is scanning the room for hotties")
        sleep(2)
        print("you know talking is futile rn.")
        return None

    if player.location != player.rooms["bathroom"]:
        if player.location == player.rooms["dance floor"]:
            print("")
            print("Music's kinda loud so they end up half shouting.")
            sleep(2)

        print("")
        print("     By the way, ", end="")
        sleep(2)
        print("I got some G, babe, ", end="")
        sleep(2)
        print("in case you want some later.")
        sleep(2)
        print("     We can't do it here in front of everyone though.")
        sleep(2)
        print("     So do consider ", end="")
        sleep(2)
        print("we'd have to go to the bathroom to take it.")
        print("")
        sleep(2)
        print("     You got that? (y/n) ", end="")
        option = yesorno()
        print("")
        if option == True:
            print("you nod.")
        elif option == False:
            print("you don't get it but you nod anyway.")
        sleep(2)
        print("")

        print("     Yeah, it's a drag, ", end="")
        sleep(2)
        print("especially when the party's packed, ", end="")
        sleep(2)
        print("but it is what it is.")
        sleep(2)
        print("     So yeah, ", end="")
        sleep(1)
        print("if you want some, just ask!")
        print("")
        player.memories.append("Ask for G")
        player.NPCs["smile"].times_talked = 2
        return True
