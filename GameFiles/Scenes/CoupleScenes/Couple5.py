from time import sleep
from ...Scripts.Blocks import items

# Youve already partied etc, this is the final link.
def coupletimes5content(player):
    if "Couple Link" in player.memories:
        print("You've had a great time with these two today.")
        print("You're really happy they could come.")
        sleep(2)
        return None
    elif "Couple Link" not in player.memories:
        print("One of them gives you a lollipop.")
        sleep(1)
        print("The other one gives you a hug.")
        sleep(1)
        print("They keep dancing to the music.")
        print("")
        sleep(2)
        print("You can tell they really needed to enjoy a good party.")
        print("You're happy you get to share tonight with them.")
        print("You know you'll remember this fondly.")
        player.memories.append("Couple Link")
        player.items.append(items["lollipop"])
        sleep(3)
        return True
