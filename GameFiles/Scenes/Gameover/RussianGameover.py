from time import sleep


def russiangameovercontent(player):
    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
    print("|                                                            |")
    print("|                                                            |")
    print("|       You're glad your russian friend was there too        |")
    if "Russian Link" in player.memories:
        print("|           it was great hanging out together again          |")
    elif "Russian Link" not in player.memories:
        print("|          you wish you could have hung out a bit more       |")
    print("|                                                            |")
    sleep(2)

    if "Russian Dance" in player.memories:
        print("|           you had so much fun on the dance floor           |")
    elif "Russian Dance" not in player.memories:
        print("|       maybe get your moves on together more next time      |")

    print("|                                                            |")
    sleep(2)

    if "Divinity" in player.memories:
        print("|                                                            |")
        print("|           you remember the red haired fairy queen          |")
        print("|                  what an absolute moment                   |")
        print("|                                                            |")
        sleep(3)

    if player.scenevariables.popper_counter >= 3:
        print("|    your head is still ringing a bit from all the poppers   |")
        print("|                                                            |")
        sleep(2)

    if player.NPCs["russian"].times_talked > 2 and (
        player.NPCs["tanktop"] not in player.people_in_party
    ):
        print("|        you didn't get to meet this mysterious friend       |")
        print("|              you're kinda curious about it                 |")

    elif player.NPCs["russian"].times_talked > 2 and (
        player.NPCs["tanktop"] in player.people_in_party
    ):
        print("|             They introduced you to the cutie               |")

        if "Tanktop Interest" in player.memories:
            print("|              so, honestly, bless their heart               |")

        elif "Tanktop Partner" in player.memories:
            print("|           your partner's def grateful about it             |")

        elif "Tanktop Conversation" in player.memories:
            print("|           and now you and your partner are in for          |")
            print("|       a conversation you had been avoiding for a while     |")

    print("|                                                            |")
    sleep(2)

    if "Russian Link" in player.memories:
        if "Attending Film Festival" in player.memories:
            print("|    You're looking forward to these film festival plans     |")
        elif "Not Attending Film Festival" in player.memories:
            print("|        You're thinking maybe you should reconsider         |")
            print("|          the film festival thing... could be fun           |")

    print("|                                                            |")
    sleep(2)

    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
    print(
        "|\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//|"
    )
