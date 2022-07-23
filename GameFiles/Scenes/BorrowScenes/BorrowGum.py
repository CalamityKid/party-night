from ...Scripts.Blocks import items


def borrowgumcontent(player):
    print("You ask one of them for chewing gum, ", end="")
    if (items["chewing gum"]) not in player.active_items and (
        items["chewing gum"]
    ) not in player.items:
        if player.scenevariables.gum_counter < 2:
            print(" the other one gives you some.")
            player.items.append(items["chewing gum"])
            player.scenevariables.popper_counter += 1
            return True

        elif player.scenevariables.gum_counter >= 3:
            print("the other one tells you they ran out.")
            return None

    elif (items["chewing gum"]) in player.active_items:
        print("you're literally chewing gum while you ask")
        print("so that doesn't get very far.")
        return None

    elif (items["chewing gum"]) not in player.items:
        print("but then you remember you already have some.")
        return None
