# already borrowed chewing gum, leaving early, set up for 4 and 5


def coupletimes2content(player):
    if player.location == player.rooms["dance floor"]:
        print("You try to talk a bit but it's very loud.")
        return None

    elif player.location != player.rooms["dance floor"]:
        if player.party.music == "terrible":
            print("     The music was okay when we got here, but now it's so bad.")
            print(
                "one of them says while the other is like, shaking their head in approval."
            )
            print("")
            print("For sure music's pretty bad right now, wish you could change it.")
            print("")
            print(
                "     We're leaving early too, like 5 am, we're gonna have to get going..."
            )
            print("     so I hope the DJ steps it up.")
            print("says the other one.")
            player.NPCs["couple"].times_talked = 3
            return True

        elif player.party.music != "terrible":
            print("     Music's okay right now, right?")
            print("says one of them.")
            print("")
            print("     Let's go dance!")
            print("says the other one and they half drag you to the dance floor.")
            print("")
            player.location = player.rooms["dance floor"]
            player.NPCs["couple"].location = player.rooms["dance floor"]
            player.NPCs["partner"].location = player.rooms["dance floor"]
            player.NPCs["couple"].times_talked = 3
            return None
