def smiledancecontent(player):
    if player.NPCs["smile"].times_talked == 5:
        print("The sound of the huge fan in the background gives you courage.")

    elif player.NPCs["smile"].times_talked == 4:
        print("The smile ambassador joins your dance.")
        print("Swinging that huge ass fan to the music.")
        print("You shadow each other's moves.")
        print("It's really very fun.")
        player.modify_stat("lit", 30, True)
        player.NPCs["smile"].boost = 1.3
        player.memories.append("Smile Dance")
        player.NPCs["smile"].times_talked = 5
