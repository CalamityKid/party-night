from time import sleep


def convincedcontent(player):
    print("     Hello darlings, having fun tonight?")
    print("")
    sleep(2)
    print("you say the music's kinda fucking with you.")
    print("and they absolutely mean it when they reply")
    print("that the music's great tonight.")
    sleep(2)
    print("")
    print("your partner explains you're planning a takeover")
    print("on the dance floor and the smile ambassador stats laughing.")
    sleep(2)
    print("     Yeah, sign me up! I'm there.")
    sleep(1)
    print("     I'll meet you down there then loves.")
    print("")
    print("and they head out.")
    sleep(2)
    player.NPCs["smile"].convinced = True
    player.NPCs["smile"].location = player.rooms["dance floor"]
    return True
