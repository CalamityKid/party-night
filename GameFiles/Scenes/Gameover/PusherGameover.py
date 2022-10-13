from time import sleep


def pushergameovercontent(player):
    if player.NPCs["pusher"] not in player.people_in_party:
        return None
    print("| X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X |")
    print("|/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \|")
    print("|\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /|")
    print("| X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X |")
    print("|/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \|")
    print("|                                                            |")
    print("|             You met your new mercantile friend             |")
    print("|               all work and no play, this one               |")
    print("|                                                            |")
    sleep(2)

    if "Commission" in player.memories:
        print("|              you helped each other out tonight             |")
        print("|                and they were sweet as balls                |")
        sleep(2)
        print("|                                                            |")
        print("|     you're looking forward to seeing them around again     |")

    elif "Pusher Business" in player.memories:
        print("|              you helped each other out tonight             |")
        print("|           you never did get your cut out of that           |")
        print("|            you'll have to remind them next time            |")

    elif "Looking for Pusher" in player.memories:
        print("|           You consider you could have connected            |")
        print("|              the cutie in the tanktop's group              |")
        print("|              with this fledgling entrepreneur              |")
        sleep(3)
        print("|          but it was none of your business, really          |")
        sleep(2)
        print("(|                          right?                           |)")

    else:
        print("|       it did't really go much deeper than that though      |)")
        sleep(2)
        print("|                  Oh well, maybe next time                  |")

    sleep(2)
    print("|                                                            |")
    print("|                                                            |")
    print("|\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /|")
    print("| X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X |")
    print("|/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \|")
    print("|\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /|")
    print("| X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X |")
