def russianflirtcontent(player):
    if player.NPCs["russian"].flirt == 3:
        print("You playfully give each other one quick kiss on the mouth.")
        return None
    elif player.NPCs["russian"].flirt == 2:
        print("You ask about all those leather straps in hard to reach places")
        print("They answer you'll have to come see for yourself.")
        player.NPCs["russian"].flirt += 1
        return None
    elif player.NPCs["russian"].flirt == 1:
        print("You do this exagerated seductive wink from afar")
        print("they cartoonishly grab their chest with both hands")
        player.NPCs["russian"].flirt += 1
        return None
    elif player.NPCs["russian"].flirt == 0:
        print("You tell your russian friend you're really into this outfit")
        print("they're glad cause it took forever to put on")
        print("You ask if they can show you how to take it off")
        print("They blush and send you an air kiss")
        player.NPCs["russian"].flirt += 1
        return None
