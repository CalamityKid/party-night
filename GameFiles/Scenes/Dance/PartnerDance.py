def partnerdancecontent(player):
    if "Changed Music" not in player.memories:
        if "Gathering" in player.memories and scriptforfriendsondancefloor is True:
            return changethemusicscene and make sure Changed Music is added to memories then

    elif player.NPCs["partner"].boost == 1.3  and player.NPCs["partner"].times_talked < 3:
        print("your partner's feeling the rhythm ")
        sleep(2)
        print("commuting with the melody sprites")
        sleep(2)
        print("effortlessly melting into the ether ")
        sleep (2)
        print("speaking with the elements")
        sleep(1)
        print("melding into the sound waves")
        sleep(2)
        print("absolute rapture")
        sleep (2)
        print ("")
        print("and it fills you with joy")
        print("your heart swells")
        sleep(2)
        player.modify_stat("lit", 10, True)
        player.modify_stat("coolness", 10, False)
        player.NPCs["partner"].times_talked = 3
        player.memories.append("Partner Dance")
        return True
    else:
        print ("your partner's dancing next to you")