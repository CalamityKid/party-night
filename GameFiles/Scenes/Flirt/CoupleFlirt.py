from time import sleep


def coupleflirtcontent(player):
    if player.NPCs["couple"].flirt == 3:
        print("You blow them air kisses")
        print("they blow you some back")
        return None
    elif player.NPCs["couple"].flirt == 2:
        print("Your wink to one of them seductively")
        print("they put the back of their hand to their face")
        print("and make a duckface")
        player.NPCs["couple"].flirt += 1
        return None
    elif player.NPCs["couple"].flirt == 1:
        print("You start making up this really convoluted compliment.")
        print("one of them misunderstands what you meant")
        print("")
        print("you end talking about the women's liberation movement somehow")
        sleep(2)
        print("for like 10 minutes")
        print("and you enjoy it")
        player.time.ten_minutes()
        if player.NPCs["couple"].boost <= 1.2:
            player.NPCs["couple"].boost = 1.2
        player.NPCs["couple"].flirt += 1
        player.modify_stat("lit", 10, True)
        return True
    elif player.NPCs["couple"].flirt == 0:
        print("You start flirting with one of them")
        print("the other one is too distracted to notice")
        player.NPCs["couple"].flirt += 1
        return None
