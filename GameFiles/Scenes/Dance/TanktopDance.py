def tanktopdancecontent(player):
    if "Tanktop Interest" in player.memories:
        if player.NPCs["tanktop"].flirt > 5:
            print("You see the cutie in the tanktop and friends dancing close to you.")

        elif player.NPCs["tanktop"].times_talked == 5:
            print("The cutie in the tanktop's group is having fun. It cheers you up.")
            return True

        elif (
            player.NPCs["tanktop"].times_talked == 4
            and "Tanktop Dance" not in player.memories
        ):
            print("You and your partner dance your way to them and join in.")
            print("The cutie's got this disco vibe going on.")

            player.memories.append("Tanktop Dance")
            player.NPCs["tanktop"].times_talked = 5
            if player.NPCs["tanktop"].boost < 1.1:
                player.NPCs["tanktop"].boost = 1.1
            player.modify_stat("lit", 20, True)
            player.modify_stat("coolness", 20, True)

            if player.NPCs["tanktop"].flirt > 3:
                print("The three of you dance together, some kissing happens too.")
                print("It's playful and sexy.")
                player.NPCs["tanktop"].flirt += 1

            return True

        elif (
            "Tanktop Conversation" in player.memories
            or "Tanktop Partner" in player.memories
        ):
            print("You, your partner and the cutie start dancing,")
            print("their whole group's cheering. It's pretty fun.")
            if player.NPCs["tanktop"].boost < 1.1:
                player.NPCs["tanktop"].boost = 1.1
            player.modify_stat("lit", 10, True)
