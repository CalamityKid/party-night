from time import sleep


def russiandancecontent(player):
    if (
        "poppers" in player.active_items
        and "Poppers First Dance" not in player.memories
    ):
        print("")
        print("you feel the rush")
        sleep(1)
        print("You let go and ride the wave, your body does its thing.")
        sleep(2)
        print("Your russian friend makes a face with his tongue out at you.")
        sleep(2)
        print("They know what's up.")
        print("")
        player.modify_stat("coolness", 30, False)
        player.memories.append("Poppers First Dance")
        return True

    elif player.NPCs["russian"].boost == 1.3:
        print("Seeing your russian friend quietly vibing nearby hypes you up.")
        return True

    elif player.NPCs["russian"].boost == 1.2:
        print("You hear YAAS BIITCH over the sound of the music")
        sleep(1)
        print("very excited but also like neutral somehow")
        sleep(1)
        print("")
        print("you turn around and your russian friend is hyping you up")
        sleep(1)
        print("you give it your all")
        player.modify_stat("lit", 20, True)
        player.NPCs["russian"].boost = 1.3
        player.memories.append("Russian Dance")
        player.time.ten_minutes()
        return True
    else:
        print("Your russian friend's riding the sound waves.")
