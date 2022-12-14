from time import sleep


def convincedcontent(player):
    print("and they tell you")
    print("")
    print("     You wanna go down to the dance floor, baabes?")
    print("")
    sleep(2)
    print("you and your partner laugh")
    print("and tell your friend your plan")
    sleep(2)
    print("")
    print("     Suure, I'm doown. See you there.")
    print("")
    sleep(2)
    print("and heads to the dance floor.")
    print("")

    player.NPCs["russian"].convinced = True
    player.NPCs["russian"].location = player.rooms["dance floor"]
    return True
