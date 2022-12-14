from time import sleep


def russiantimes0content(player):
    print("")
    print("     Heeey bitchees! ", end="")
    sleep(2)
    print("You guys doing alriiight?")
    print("")
    sleep(2)
    print("in that way your russian friend speaks")
    sleep(2)
    print("like really into it but also in a totally neutral tone of voice.")
    print("")
    print("Both you and your partner agree things are, indeed, alriiight.")
    sleep(2)
    print("you talk for a bit about how the week went and such")
    player.NPCs["russian"].times_talked = 1
    return False
