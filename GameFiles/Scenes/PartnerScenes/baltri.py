from concurrent.futures.process import _threads_wakeups
from time import sleep

# should play immediately if high reaches 100


def baltricontent(player):
    print("your mind starts drifting from your body")
    sleep(2)
    print("your arms and legs don't quite respond")
    sleep(2)
    print("")
    print("so lightheaded")
    sleep(2)
    print("")
    print("and you start losing balance")
    print("you try to get a grip")
    sleep(4)
    print("")
    print("your partner sees it in your eyes")

    if "Too High" in player.memories:
        print("again. on the same night.")
        sleep(2)

    print("grabs you by the arm")
    print("")
    sleep(4)
    print("and suddenly you wake up on the floor")
    sleep(2)
    print("your partner and your russian friend are there")
    sleep(2)
    print("they look very concerned")
    print("")
    sleep(3)
    if player.time.hour > 5 and player.time.minutes > 30:
        print("you're outside the club")
        sleep(2)
        print("the party's over already")
        print("")
        sleep(2)

    if "Too High" in player.memories:
        print("you feel so embarrased.")
        sleep(2)
        print("you realize you might have a problem with drugs...")
        print("")
        sleep(2)
        player.gameover = True
        player.memories.append("Too High Twice")

    print("they make you drink some water")
    sleep(2)
    print("they ask you many many times")
    sleep(1)
    print("if you feel okay, if you need anything")
    print("")
    sleep(4)
    print("and you do feel better")
    sleep(2)
    print("you tell them you're okay")
    sleep(2)
    print("thanks and sorry, you're okay now")
    sleep(3)
    print("")
    print("you realize it's been at least half an hour")
    print("what a mess")
    sleep(4)
    print("")

    player.modify_stat("high", 70, False)
    player.modify_stat("mouth", 40, True)
    if "Too High" not in player.memories:
        player.memories.append("Too High")
    if "Too High Twice" in player.memories:
        print("")
        print("     You decide to leave the party.")
    player.time.ten_minutes()
    player.time.ten_minutes()
    return True
