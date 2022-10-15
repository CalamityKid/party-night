from time import sleep


def convincedcontent(player):
    print("and tell them you have a plan")
    print("")
    sleep(1)
    print("""     Is this one of your "great ideas"? """)
    print("one of them says while the other chuckles")
    print("")
    sleep(2)
    print("your partner starts")
    print("     Remember that party at the warehouse out of town?")
    sleep(2)
    print("one of them says they didn't go to that party")
    print("the other one says they remember the story though")
    sleep(3)
    print("     It's the same DJ, nobody's dancing down there.")
    print("     it might work...")
    print("")
    sleep(2)
    print("one of them shrugs, the other one sighs")
    print("     Sure, why not, it cannot get any worse than this.")
    print("     I'll go find the rest of the gang.")
    sleep(2)
    print("")
    print("and they both head to the dance floor.")
    sleep(2)

    player.NPCs["couple"].convinced = True
    player.NPCs["couple"].location = player.rooms["dance floor"]
    return True
