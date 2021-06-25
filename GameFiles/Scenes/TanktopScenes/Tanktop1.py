# this node is basically a reaffirmation of the partner choose-your-path node


def tanktoptimes1content(player):
    if (
        "Tanktop Conversation" not in player.memories
        and "Tanktop Interest" not in player.memories
        and "Tanktop Partner" not in player.memories
    ):
        print(
            "Maybe you should talk to your partner somewhere else before you make a move."
        )
        return None

    else:
        print("You search around the room and make eye contact")
        print("the cutie's with a group of friends")
        print("and they do this thing, between a smile and biting their lip")
        print("Yeah...")
        print("")
        print("You walk up to their group and you smile")
        if "Tanktop Conversation" in player.memories:
            print("as harmlessly as you can")
            print("the way you'd smile to a family member.")
            print("")
            print("You can tell they notice.")
        elif "Tanktop Interest" in player.memories:
            print("a devilish smile")
            print("you really put some weight behind it")
            print("")
            print("and it works.")
            player.NPCs["tanktop"].flirt += 2
        elif "Tanktop Partner" in player.memories:
            print("pretty harmlessly, you lay back")
            print("and your partner takes over")
            print("")
            print("you act as support.")
        print("")
        if player.location == player.rooms["dance floor"]:
            print("You half shout half sign language over the music")

        elif player.location != player.rooms["dance floor"]:
            print("You talk a bit about how the party's going")

        print(
            "The cutie tells you, a friend of theirs, who was bringing the candy flaked on their group."
        )
        print("They're all pretty visibly upset about it.")
        player.NPCs["tanktop"].times_talked = 2
        return True
