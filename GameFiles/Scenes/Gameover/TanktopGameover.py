def tanktopgameovercontent(player):
    if player.NPCs["tanktop"] not in player.people_in_party:
        return None
    print("|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|                                                            |")
    print("|          You met the cutie in the tanktop tonight          |")

    if "Tanktop Interest" in player.memories:
        print("|                  this absolute dream babe.                 |")

    elif "Tanktop Partner" in player.memories:
        print("|          your partner's specially happy about that.        |")

    elif "Tanktop Conversation" in player.memories:
        print("|              your partner seems upset about it             |")
        print("|           looks like you're gonna be talking about         |")
        print("|            the nature of your relationship soon...         |")

    print("|                                                            |")

    if "Tanktop Link" in player.memories:
        print("|          You got to know them a bit, they seem cool        |")
    elif (
        "Tanktop Link" not in player.memories and "Tanktop Home" not in player.memories
    ):
        print("|          You didn't talk to the cutie that much...         |")

    if "Pusher Business" in player.memories:
        print("|            their friends were fun, if a bit loud           |")
        print("|                they were happy as heck with you            |")
    elif "Looking for Pusher" in player.memories:
        print("|   their friends were so centered on how sober they were    |")
        print("|             they didn't even try having any fun.           |")
        print("|                    It's a shame really...                  |")
    print("")

    if "Tanktop Dance" in player.memories:
        print("|      and you def enjoyed your time on the dance floor      |")
    elif "Tanktop Dance" not in player.memories:
        print("|         you didn't get to party together that much         |")
    print("|                                                            |")

    if "Tanktop Interest" in player.memories:
        if player.NPCs["tanktop"].flirt >= 6:
            print("|       there's great chemistry between the three of you     |")
        elif player.NPCs["tanktop"].flirt < 6:
            print("|              your flirt game was so weak though            |")
        print("|                                                            |")

    elif "Tanktop Partner" in player.memories:
        print("|        Your partner and the cutie really hit it off        |")
        print("||")
        if "Partner Hookup" in player.memories:
            print("|             they even got to fool around a bit             |")
            feelingstr = (
                "|                  it made you feel "
                + str(player.PartnerHookupFeeling)
                + "."
            )
            print(str(feelingstr))

    if "TanktopAsks" in player.memories and "Tanktop Home" not in player.memories:
        print("|               they wanted to come home with you            |")
        print("|                maybe you'll text them later                |")

    elif "Tanktop Home" in player.memories:
        print("|            you are now on your way home together           |")
        print("|                    looking forward to it!                  |")

    print("|                                                            |")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
