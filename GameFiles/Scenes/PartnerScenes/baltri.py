# should play immediately if high reaches 100


def baltricontent(player):
    print("your mind starts drifting from your body")
    print("your arms and legs don't quite respond")
    print("so lightheaded")
    print("and you start losing balance")
    print("you try to get a grip")
    sleep(4)
    print("your partner sees it in your eyes")

    if "Too High" in player.memories:
        print("again. on the same night.")
        print("")

    print("grabs you by the arm")
    print("")
    sleep(3)
    print("and suddenly you wake up on the floor")
    print("your partner and your russian friend are there")
    print("they look very concerned")
    print("")
    if player.time.hour > 5 and player.time.minutes > 30:
        print("you're outside the club")
        print("the party's over already")

    if "Too High" in player.memories:
        print("you feel so embarrased.")
        print("you realize you might have a problem...")
        print("")
        sleep(2)

    print("they make you drink some water")
    print("they ask you many many times")
    print("if you feel okay, if you need anything")
    print("")
    sleep(1)
    print("and you do feel better")
    print("you tell them you're okay ")
    print("thanks and sorry, you're okay now")
    print("")
    print("you realize it's been at least half an hour")
    print("what a mess")

    player.modify_stat("high", 50, False)
    player.modify_stat("mouth", 40, True)
    player.memories.append("Too High")
    player.time.ten_minutes()
    player.time.ten_minutes()
    return True
