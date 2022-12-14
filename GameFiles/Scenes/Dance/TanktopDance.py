from time import sleep


def tanktopdancecontent(player):
    if "Tanktop Interest" in player.memories:

        if player.NPCs["tanktop"].times_talked == 5:
            print("The cutie in the tanktop's group is having fun. It cheers you up.")
            return True

        elif (
            player.NPCs["tanktop"].times_talked == 4
            and "Tanktop Dance" not in player.memories
        ):
            print("You and your partner dance your way to them and join in.")
            sleep(2)
            print("The cutie's got this disco vibe going on")
            sleep(1)
            print("you two catch the fever, disco fingers and all")
            sleep(1)
            print("it's hella fun")
            player.time.ten_minutes()

            player.memories.append("Tanktop Dance")
            player.NPCs["tanktop"].times_talked = 5
            if player.NPCs["tanktop"].boost < 1.1:
                player.NPCs["tanktop"].boost = 1.1
            player.modify_stat("lit", 20, True)
            player.modify_stat("coolness", 20, True)

            if player.NPCs["tanktop"].flirt > 3:
                print("The three of you dance together, some kissing happens too.")
                sleep(1)
                print("It's playful and sexy.")
                player.NPCs["tanktop"].flirt += 2
            return True

    elif (
        "Tanktop Conversation" in player.memories
        or "Tanktop Partner" in player.memories
    ) and player.NPCs["tanktop"].boost < 1.1:
        print("You, your partner and the cutie start dancing,")
        sleep(1)
        print("their whole group's cheering. It's pretty fun.")
        if player.NPCs["tanktop"].boost < 1.1:
            player.NPCs["tanktop"].boost = 1.1
        player.modify_stat("lit", 20, True)
        return True
    else:
        print("You see the cutie in the tanktop and friends dancing close to you.")
