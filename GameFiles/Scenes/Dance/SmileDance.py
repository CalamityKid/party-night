from time import sleep


def smiledancecontent(player):
    if player.NPCs["smile"].times_talked == 5:
        print("The sound of the huge fan in the background gives you courage.")

    elif player.NPCs["smile"].times_talked == 4:
        print("The smile ambassador joins your dance.")
        sleep(1)
        print("Swinging that huge ass fan to the music.")
        sleep(1)
        print("You shadow each other's moves.")
        sleep(1)
        print("It's really very fun.")
        player.modify_stat("lit", 30, True)
        player.NPCs["smile"].boost = 1.3
        player.memories.append("Smile Dance")
        player.NPCs["smile"].times_talked = 5
        player.time.ten_minutes()
        return True

    else:
        print("The smile ambassador sways close to you.")
