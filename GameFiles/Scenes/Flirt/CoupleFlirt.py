from time import sleep


def coupleflirtcontent(player):
    if player.NPCs["couple"].flirt == 3:
        print("You blow them air kisses")
        sleep(2)
        print("they blow you some back")
        return None
    elif player.NPCs["couple"].flirt == 2:
        print("Your wink to one of them seductively")
        sleep(2)
        print("they put the back of their hand to their face")
        sleep(2)
        print("and make a duckface")
        player.NPCs["couple"].flirt += 1
        return None
    elif player.NPCs["couple"].flirt == 1:
        print("You start making up this really convoluted compliment.")
        sleep(2)
        print("one of them misunderstands what you meant")
        sleep(2)
        print("")
        print("you end talking about the women's liberation movement somehow")
        sleep(2)
        print("for like 10 minutes")
        sleep(2)
        print("and you really enjoy the conversation")
        print("")
        player.time.ten_minutes()
        if player.NPCs["couple"].boost <= 1.2:
            player.NPCs["couple"].boost = 1.2
        player.NPCs["couple"].flirt += 1
        player.modify_stat("lit", 10, True)
        return True
    elif player.NPCs["couple"].flirt == 0:
        print("You start fake flirting with one of them")
        sleep(2)
        print("the other one is too distracted to notice")
        player.NPCs["couple"].flirt += 1
        return None
