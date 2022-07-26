from random import randint


def pusherflirtcontent(player):
    if player.NPCs["pusher"].flirt == 0:
        print("you get a half smirk back")
        print("")
        print("     Don't think that'll get you any discounts though!")
        print("you answer the only prize you're after is a smile")
        print("and you get your prize")
        player.NPCs["pusher"].flirt += 1
        return None
    elif (
        "Pusher Business" in player.memories
        and player.NPCs["pusher"].flirt >= 2
        and "PusherFlirtScene" not in player.memories
    ):
        print("")
        print("     You wanna sweeten the deal even more huh?")
        print("     I'm strictly business today sexy")
        print("     don't get any ideas")
        print(" ")
        print("you three laugh it off.")
        player.memories.append("PusherFlirtScene")
        player.NPCs["pusher"].flirt += 1
        return None

    else:
        rando = randint(0, 2)
        if rando == 0:
            print("You wink and smile from some distance away.")
            print("They pretend they didn't see you, but you can see the smirk.")
            player.NPCs["pusher"].flirt += 1
            return None
        elif rando == 1:
            print("You compliment their jacket.")
            print("They tell you they genuinely appreciate the compliment.")
            player.NPCs["pusher"].flirt += 1
            return None
        elif rando == 2:
            print("You can't think of anything to tell them right now.")
            return None
