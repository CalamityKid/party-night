from time import sleep


def partnertimes1content(player):
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sleep(2)
    player.modify_stat("lit", 10, True)
    player.NPCs["partner"].times_talked = 2
    return True


def partnertimes1content(player):
    if player.NPCs["couple"] not in player.people_in_party and player.time.hour < 5:
        print("Your partner tells you")
        print("    I'm glad they came tonight!")
        sleep(2)
        print("your friends, the cute couple, you assume")
        print("one of them worked late, you thought they might not come at all")
        sleep(2)
        print("They said they'll leave early, like around 5")
        print("so let's hang out and dance and have fun")
        sleep(2)
        print("you agree, the night feels promising")
        sleep(1)

    elif player.time.hour > 5:
        print("Your partner tells you")
        print("    I'm glad they did come tonight after all!")
        sleep(2)
        print("your friends, the cute couple, you assume")
        print("one of them worked late, you thought they might not come at all")
        sleep(2)
        print("it was fun hanging out ")
        print("I'm really glad we met them")
        sleep(4)
        print("you agree, it makes you feel all warm inside")
        sleep(1)
    player.modify_stat("lit", 10, True)
    player.NPCs["partner"].times_talked = 2
    return True
