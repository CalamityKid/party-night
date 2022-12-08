from time import sleep

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
        sleep(1)
        print("the cutie's with a group of friends")
        sleep(2)
        print("and they do this thing, between a smile and biting their lip")
        sleep(2)
        print("Yeah...")
        print("")
        sleep(1)
        print("You walk up to their group and you smile")
        sleep(2)
        if "Tanktop Conversation" in player.memories:
            print("as harmlessly as you can")
            sleep(1)
            print("the way you'd smile to a family member.")
            sleep(1)
            print("")
            print("You can tell they notice.")
        elif "Tanktop Interest" in player.memories:
            print("a devilish smile")
            sleep(2)
            print("you really put some weight behind it")
            sleep(2)
            print("")
            print("and it def has an effect.")
            sleep(2)
            player.NPCs["tanktop"].flirt += 2
        elif "Tanktop Partner" in player.memories:
            print("pretty harmlessly, you lay back")
            sleep(1)
            print("and your partner takes over")
            sleep(2)
            print("")
            print("you act as support.")
            sleep(2)
        print("")
        if player.location == player.rooms["dance floor"]:
            print("You half shout half sign language over the music")

        elif player.location != player.rooms["dance floor"]:
            print("You talk a bit about how the party's going")

        sleep(2)
        print("The cutie tells you a friend of theirs ", end="")
        sleep(2)
        print("who was bringing the candy ", end="")
        sleep(2)
        print("flaked on their group.")
        sleep(2)
        print("They're all pretty visibly upset about it.")
        player.NPCs["tanktop"].times_talked = 2
        return True
