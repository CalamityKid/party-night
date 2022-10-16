from time import sleep


def partnerflirtcontent(player):
    if player.NPCs["partner"].flirt == 3:
        print("you win at your partner")
        sleep(1)
        print("you get the cutest smile back")
        return None
    elif player.NPCs["partner"].flirt == 2:
        print("You start massaging your partner's shoulders")
        sleep(1)
        print("and kiss their neck softly")
        sleep(2)
        print("")
        print("you have a little moment together")
        sleep(1)
        print("you hold and kiss each other tenderly")
        sleep(1)
        print("and the party dissappears for a little while")
        sleep(3)
        print("it's just a moment but you really enjoy it.")
        sleep(2)
        player.modify_stat("lit", 20, True)
        player.NPCs["partner"].flirt += 1
        return True
    elif player.NPCs["partner"].flirt == 1:
        print("you try to flirt with your partner")
        sleep(1)
        print("but they're distracted and don't notice at all.")
        sleep(2)
        player.NPCs["partner"].flirt += 1
        return None
    elif player.NPCs["partner"].flirt == 0:
        print("")
        print("you start flirting with your partner")
        sleep(1)
        print("and you get the sweetest smile in return")
        sleep(1)
        print("")
        print("You just melt. ", end="")
        sleep(2)
        print("You've been overflirted.")
        player.modify_stat("lit", 10, True)
        player.NPCs["partner"].flirt += 1
        return None
