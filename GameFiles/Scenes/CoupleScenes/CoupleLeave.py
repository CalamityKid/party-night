def coupleleavescontent(player):
    print("The cute couple walks up to you and your partner")
    print("")
    print("     Babes, we gotta go, it's 5 already")
    print("says one of them while the other hugs you")

    if "Couple Dance" in player.memories:
        print("     It was fun!")

    elif "Couple Dance" not in player.memories:
        print("     Maybe they'll have better music next time")
    print("one of them says")

    if "Couple Link" in player.memories:
        print("     It was great to hang out love!")
        print("the other one says")

    print("They hug everyone goodbye and leave the party.")
    player.NPCs["couple"].location = None
    player.people_in_party.remove(player.NPCs["couple"])
    return None
