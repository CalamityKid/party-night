from time import sleep


def couplegameovercontent(player):
    if player.NPCs["couple"].times_talked == 0:
        return None
    print("|(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )|")
    print("| )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )( |")
    print("|(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )|")
    print("| )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )( |")
    print("|                                                            |")
    print("|                                                            |")
    print("|       You got to see your friends, the cute couple,        |")

    if "Couple Link" in player.memories:
        print("|       you got to share some great moments with them        |")
    elif "Couple Link" not in player.memories:
        print("|      you wish you could have spent more time with them     |")
    print("|                                                            |")
    sleep(2)

    if "Changed Music" in player.memories:
        print("|         you'll never forget how excited they got           |")
        print("|       when you got the DJ to play something decent,        |")

    elif "Couple Convinced" in player.memories:
        print("|         even though the music sucked, it was nice          |")
        print("|              to get them on the dance floor,               |")
    print("|                                                            |")
    sleep(2)

    if "Couple Dance" in player.memories:
        print("|             dancing with them was so much fun.             |")
    elif "Couple Dance" not in player.memories:
        print("|      you wish you could have really danced with them.      |")
    print("|                                                            |")
    sleep(2)

    print("|                                                            |")
    print("|(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )|")
    print("| )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )( |")
    print("|(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )|")
    print("| )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )(  )( |")
