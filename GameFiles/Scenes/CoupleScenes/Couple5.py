from ...Scripts.Blocks import items

# Youve already partied etc, this is the final link.
def coupletimes5content(player):
    if "Couple Link" in player.memories:
        print("You've had a great time with these two today.")
        print("You're really happy they could come.")
        return None
    elif "Couple Link" not in player.memories:
        print("One of them gives you a lollipop.")
        print("The other one gives you a hug.")
        print("They keep dancing to the music.")
        print("")
        print("You can tell they really needed to enjoy a good party.")
        print("You're happy you get to share tonight with them.")
        print("You know you'll remember this fondly later.")
        player.memories.append("Couple Link")
        player.items.append(items["lollipop"])
        return True
