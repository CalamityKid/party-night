from time import sleep


def coupleleavescontent(player):
    print("The cute couple walks up to you and your partner")
    print("")
    sleep(2)
    print("     Babes, we gotta go, it's 5 already")
    sleep(2)
    print("says one of them while the other hugs you")
    sleep(3)
    print("")

    if "Couple Dance" in player.memories or "Music Changed" in player.memories:
        print("     It was fun!")

    elif "Couple Dance" not in player.memories:
        print("     Maybe they'll have better music next time")
    sleep(2)
    print("one of them says")
    print("")

    if "Couple Link" in player.memories:
        print("     It was great to hang out love!")
        sleep(2)
        print("the other one says")
        sleep(3)
        print("")

    print("They hug everyone goodbye and leave the party.")
    player.NPCs["couple"].location = None
    player.people_in_party.remove(player.NPCs["couple"])
    player.memories.remove("Borrow Gum")
    return None
