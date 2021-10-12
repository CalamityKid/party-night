def tanktopgameovercontent(player):
    if player.NPCs["tanktop"] not in player.people_in_party:
        return None
    print("|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|                                                            |")
    print("|          You met the cutie in the tanktop tonight          |")

    if "Tanktop Hookup" in player.memories:
        print("|                this absolute dream cutie.                  |")
    elif "Tanktop Interest" in player.memories:
        print("|         you hope you get to see them again soon.           |")
    elif "Partner Hookup" in player.memories:
        print("|                your partner had their fun.                 |")
    elif "Tanktop Partner" in player.memories:
        print("|    your partner's looking forward to meeting them again.   |")
    elif "Tanktop Conversation" in player.memories:
        print("|           your partner seems pretty upset with you         |")
        print("|           you're gonna be talking about the nature         |")
        print("|           of your relationship together very soon.         |")

    print("|                                                            |")

    if "Tanktop Link" in player.memories:
        print("|          You got to know them a bit, they seem cool        |")
    elif (
        "Tanktop Link" not in player.memories and "Tanktop Home" not in player.memories
    ):
        print("|            You didn't get their contact though...          |")

    if "Pusher Business" in player.memories:
        print("|            their friends are fun too, if a bit loud        |")
        print("|                they were happy as heck with you            |")
    elif "Looking for Pusher" in player.memories:
        print("|          their friends were so centered on the candy       |")
        print("|             they didn't even try having any fun.           |")
        print("|                    It's a shame really...                  |")

    if "Tanktop Dance" in player.memories:
        print("|        you def enjoyed your time on the dance floor        |")
    elif "Tanktop Dance" not in player.memories:
        print("|         you didn't get to party together properly          |")

    print("|                                                            |")
    if "Tanktop Interest" in player.memories:
        if player.player.NPCs["tanktop"].flirt >= 6:
            print("|       there's great chemistry between the three of you     |")
        elif player.player.NPCs["tanktop"].flirt < 6:
            print("|              your flirt game was so weak though            |")
        print("|                                                            |")

    if "Tanktop Home" in player.memories:
        print("|            you are now on your way home together           |")
        print("|                    looking forward to it!                  |")

    print("|                                                            |")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")
    print("|<> <> <> <> <> <> <> <> <> <>  <> <> <> <> <> <> <> <> <> <>|")
    print("|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
