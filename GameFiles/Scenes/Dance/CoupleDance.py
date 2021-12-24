def coupledancecontent(player):
    if player.NPCs["couple"].times_talked == 5:
        print("The cute couple's enthusiasm gives you inspiration.")

    elif player.NPCs["couple"].times_talked == 4:
        if player.party.music == "terrible":
            print("The cute couple's next to you")
            print("one of them's having a really hard time with the music")
            print("")
            print("You start dancing like an idiot")
            print("making fun of how bad the music is")
            print("the other one joins in the dance")
            print("it ends up being pretty fun")
            print("")
            player.modify_stat("coolness", 30, False)

        elif player.party.music is not "terrible":
            print("The cute couple's really having a blast with this new music")
            print("they both end up joining you on this crazy performance piece")
            print("It's pretty cool actually")
            print("")
            player.modify_stat("coolness", 40, False)
            player.memories.append("Couple Dance")
            player.NPCs["couple"].boost = 1.3
            player.NPCs["couple"].times_talked = 5

    elif (
        (player.time.hour == 2 and player.time.minute >= 30)
        or (player.time.hour == 4 and player.time.minute <= 30)
    ) and player.NPCs["couple"].times_talked < 4:
        print("The cute couple's dancing next to you")
        print("one of them offers you some of their water")
        print("")
        print("You take a big gulp")
        print("bless them.")
        player.modify_stat("mouth", 30, True)
