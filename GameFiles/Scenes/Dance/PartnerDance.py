from time import sleep


def partnerdancecontent(player):

    if player.NPCs["partner"].times_talked == 5:
        print("your partner's in communion with the music")
        return True

    elif player.NPCs["partner"].times_talked == 4:
        print("you join in your partner in dance")
        return True

    elif (
        player.NPCs["partner"].boost == 1.3 and player.NPCs["partner"].times_talked < 3
    ) and "Partner Dance" not in player.memories:
        print("your partner's feeling the rhythm ")
        sleep(2)
        print("commuting with the melody sprites")
        sleep(2)
        print("effortlessly melting into the ether ")
        sleep(2)
        print("speaking with the elements")
        sleep(1)
        print("melding into the sound waves")
        sleep(2)
        print("absolute rapture")
        sleep(2)
        print("")
        print("and it fills you with joy")
        print("your heart swells")
        player.modify_stat("lit", 10, True)
        player.modify_stat("coolness", 10, False)
        player.NPCs["partner"].times_talked = 3
        player.memories.append("Partner Dance")
        return True
    else:
        print("your partner's dancing next to you")
        return True
