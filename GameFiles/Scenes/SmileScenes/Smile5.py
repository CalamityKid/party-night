# Youve already partied etc, this is the final link.


def smiletimes5content(player):
    print("")
    if "Smile Link" in player.memories:
        print("You've shared some great memories tonight.")
        print("You feel really grateful for your friendship.")
        print("")
        return None
    elif "Smile Link" not in player.memories:
        if player.location == player.rooms["dance floor"]:
            print(
                "You're lead to a corner of the room so you don't have to scream over the music."
            )
        elif player.location != player.rooms["dance floor"]:
            print(
                "The smile ambassador goes all serious for a second and looks at you."
            )
        print(
            "     You know, when I first met you last march. I did think you were cool."
        )
        print("     But I not this cool.")
        print("")
        print("     What I mean to say is...")
        print("     I'm really glad we get to share. It's great to party together too.")
        print("     I'm really happy we've become good friends.")
        print("You feel the same way. You hug and go back to the party.")
        print(" ")
        print("You know you'll remember this tenderly later'.")
        player.memories.append("Smile Link")
        return True
