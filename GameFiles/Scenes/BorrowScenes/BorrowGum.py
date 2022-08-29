from ...Scripts.Blocks import items
from time import sleep


def borrowgumcontent(player):
    print("You ask one of them for chewing gum, ", end="")
    if (items["chewing gum"]) not in player.active_items and (
        items["chewing gum"]
    ) not in player.items:
        if player.scenevariables.gum_counter < 2:
            print(" the other one gives you some.")
            sleep(2)
            print("You put the chewing gum in your pocket.")
            sleep(2)
            player.items.append(items["chewing gum"])
            player.scenevariables.gum_counter += 1
            return True

        elif player.scenevariables.gum_counter >= 2:
            print("the other one tells you they ran out.")
            return None

    elif (items["chewing gum"]) in player.active_items:
        print("you're literally chewing gum while you ask")
        sleep(2)
        print("so that doesn't get very far.")
        sleep(2)
        return None

    elif (items["chewing gum"]) in player.items:
        print("but then you remember you already have some.")
        return None
