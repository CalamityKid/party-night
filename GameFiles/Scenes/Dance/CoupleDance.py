from time import sleep


def coupledancecontent(player):
    if player.NPCs["couple"].times_talked == 5:
        print("The cute couple's enthusiasm gives you inspiration.")
        return True

    if player.NPCs["couple"].times_talked == 4:
        if player.party.music == "terrible" and "Dumb Dance" not in player.memories:
            print("The cute couple's next to you")
            sleep(2)
            print("one of them's having a really hard time with the music")
            print("")
            sleep(2)
            print("You start dancing like an idiot")
            sleep(2)
            print("making fun of how bad the music is")
            sleep(2)
            print("the other one joins in the dance")
            sleep(2)
            print("it ends up being pretty fun")
            sleep(2)
            player.modify_stat("coolness", 30, False)
            player.memories.append("Dumb Dance")
            return True

        if player.party.music != "terrible":
            print("The cute couple's really having a blast with this new music")
            sleep(2)
            print("they both end up joining you on this crazy performance piece")
            sleep(2)
            print("It's pretty cool actually")
            sleep(2)
            player.modify_stat("coolness", 40, False)
            player.memories.append("Couple Dance")
            player.NPCs["couple"].boost = 1.3
            player.NPCs["couple"].times_talked = 5
            player.time.ten_minutes()
            return True

    if (
        (player.time.hour == 2 and player.time.minute >= 30)
        or (player.time.hour == 4 and player.time.minute <= 30)
    ) and player.NPCs["couple"].times_talked < 4:
        print("The cute couple's dancing next to you")
        sleep(2)
        print("one of them offers you some of their water")
        print("")
        sleep(2)
        print("You take a big gulp")
        sleep(1)
        print("bless them.")
        player.modify_stat("mouth", 30, True)
        sleep(2)
        return True
    else:
        print("Your friends, the cute couple, are dancing by your side.")
        return True
