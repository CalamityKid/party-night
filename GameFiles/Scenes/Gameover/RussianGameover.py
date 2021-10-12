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
    print("|       You're glad your russian friend was there too        |")
    if "Russian Link" in player.memories:
        print("|           it was great hanging out together again          |")
    elif "Russian Link" not in player.memories:
        print("|          you wish you could have hung out a bit more       |")

    if "Russian Dance" in player.memories:
        print("|           you had so much fun on the dance floor           |")
    elif "Russian Dance" not in player.memories:
        print("|       maybe get your moves on together more next time      |")

    if "Divinity" in player.memories:
        print("|                                                            |")
        print("|           you remember the red haired fairy queen          |")
        print("|                  what an absolute moment                   |")
        print("|                                                            |")

    if player.scenevariables.popper_counter >= 3:
        print("|    your head is still ringing a bit from all the poppers   |")
        print("|                                                            |")

    if player.NPCs["russian"].times_talked > 2 and (
        player.NPCs["tanktop"] not in player.people_in_party
    ):
        print("|        you didn't get to meet this mysterious friend       |")
        print("|              you're kinda curious about it                 |")
        print("|                                                            |")
    elif player.NPCs["russian"].times_talked > 2 and (
        player.NPCs["tanktop"] in player.people_in_party
    ):
        print("|             They introduced you to the cutie               |")
        if "Tanktop Hookup" in player.memories:
            print("|        and that turned out pretty great for you two        |")
        elif "Tanktop Interest" in player.memories:
            print("|          you hope you get to see them again soon           |")
        elif "Partner Hookup" in player.memories:
            print("|           and your partner def had a good time             |")
        elif "Tanktop Partner" in player.memories:
            print("|            you partner's def grateful about it             |")
        elif "Tanktop Conversation" in player.memories:
            print("|           and now you and your partner are in for          |")
            print("|       a conversation you had been avoiding for a while     |")
        print("|                                                            |")

    if "Attending Film Festival" in player.memories:
        print("|        You're definitely looking forward to going          |")
        print("|         to that film festival together next week!          |")

    elif "Not Attending Film Festival" in player.memories:
        print("|           You're thinking of maybe reconsidering           |")
        print("|            the whole film festival thing later.            |")

    print("|                                                            |")
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
