from time import sleep

# Youve already partied etc, this is the final link.


def smiletimes5content(player):
    print("")
    if "Smile Link" in player.memories:
        print("You've shared some fun moments tonight.")
        sleep(2)
        print("You feel really grateful for your friendship.")
        print("")
        return None
    elif "Smile Link" not in player.memories:
        if player.location == player.rooms["dance floor"]:
            print("You're lead to a corner of the room ", end="")
            sleep(2)
            print("so you don't have to scream over the music.")

        elif player.location != player.rooms["dance floor"]:
            print("The smile ambassador goes all serious for a second", end="")
            sleep(2)
            print("and looks at you.")

        sleep(2)
        print("")
        print("     You know, when I first met you guys last march.")
        sleep(2)
        print("I did think you were cool.")
        sleep(2)
        print("     But not this cool.")
        sleep(2)
        print("")
        sleep(2)
        print("     What I mean to say is...")
        sleep(2)
        print("     Maybe it's the drugs too, but")
        sleep(2)
        print("     I'm really glad we get to share. ", end="")
        sleep(2)
        print("It's great to party together too.")
        sleep(2)
        print("     I'm really happy we've become close.")
        sleep(2)
        print("")
        print("You feel the same way. ", end="")
        sleep(2)
        print("Truly. ", end="")
        sleep(1)
        print("You hug and go back to the party.")
        sleep(2)
        print(" ")
        print("You know you'll remember this tenderly later.")
        player.memories.append("Smile Link")
        return True
