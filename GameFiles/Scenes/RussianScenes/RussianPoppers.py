from random import randint
from ...Scripts.Blocks import items
from ...Scripts.Actions.Use_ItemSc import use_item
from ...Input import yesorno

# Only usable on dance floor


def russianpopperscontent(player):
    if player.location != player.rooms["dance floor"]:
        print("They remind you, only on the dance floor baabe, okaay?")
        print("")
        return None
    elif items["poppers"] in player.active_items:
        print("You just did some, don't wanna hoard the bottle.")
        print("")
        return None
    elif player.scenevariables.popper_counter == 5:
        print("You signal that you want to take a hit")
        print("your russian friend shrugs")
        print("you assume someone else must have the bottle.")
        print(" ")
        print("     Do you wanna look around? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("you look around a bit")
            print("your partner sees you looking around and stops dancing")
            print("wants to know whats going on")
            print("")
            print("you start to explain you're looking for the poppers")
            print("they start laughing and show you the bottle")
        elif option == False:
            print("You don't care enough to look around for it")
            print("few seconds pass and you see your partner returning the bottle")
        print("your partner had it")
        print("")
        player.scenevariables.popper_counter += 1
        player.items.append(items["poppers"])
        use_item.execute(player, items["poppers"])
        print("You return the bottle.")
        return True

    elif player.location == player.rooms["dance floor"]:
        if player.party.crowd == "empty":
            if player.time.hour < 5:
                print("You signal your friend you want a hit")
                print("they kinda look around the room")
                print("the very empty room.")
                print("Don't wanna be so obvious.")
                return None
            elif player.time.hour >= 5:
                print("You signal you want some poppers")
                print("room's empty but nobody still here cares probably")
                print("your russian friend gives you the bottle")
                player.items.append(items["poppers"])
                use_item.execute(player, items["poppers"])
                player.scenevariables.popper_counter += 1
                print("your partner also takes a deep one")
                print("you pass the bottle back.")
                return None

        elif player.party.crowd != "empty":
            op = randint(0, 3)
            if op == 0:
                print("Your russian friend opens the bottle and puts it to your nose.")
            elif op == 1:
                print("They've just taken a hit themselves")
                print(
                    "they cover up the bottle with their thumb and put it to your nose."
                )
            elif op == 2:
                print("They signal to a friend of theirs who's dancing nearby")
                print(
                    "you signal to their friend you want some and they give you the bottle."
                )
            elif op == 3:
                print("Your friend gives you the bottle.")

            player.items.append(items["poppers"])
            use_item.execute(player, items["poppers"])
            if op == 2:
                print("You give the bottle back.")
            elif op == 3:
                print("You take your tongue out and nod to them")
                print("they nod with their tongue out right back.")
            player.scenevariables.popper_counter += 1
            return None