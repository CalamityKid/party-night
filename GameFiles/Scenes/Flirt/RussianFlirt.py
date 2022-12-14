from time import sleep


def russianflirtcontent(player):
    if player.NPCs["russian"].flirt == 3:
        print("You playfully give each other one quick kiss on the mouth.")
        return None
    elif player.NPCs["russian"].flirt == 2:
        print("You ask about all those leather straps in hard to reach places")
        sleep(2)
        print("They answer you'll have to come see for yourself.")
        player.NPCs["russian"].flirt += 1
        return None
    elif player.NPCs["russian"].flirt == 1:
        print("You do this exagerated seductive wink from afar")
        sleep(2)
        print("they cartoonishly grab their chest with both hands")
        player.NPCs["russian"].flirt += 1
        return None
    elif player.NPCs["russian"].flirt == 0:
        print("You tell your russian friend you're really into this outfit")
        sleep(2)
        print("they're glad cause it took forever to put on")
        sleep(2)
        print("You ask if they can show you how to take it off")
        sleep(2)
        print("You get a good chuckle in return")
        player.NPCs["russian"].flirt += 1
        return None
