from time import sleep
from ...Scripts.Blocks.ItemsSc import items

# Youve just been introduced.
# There are two memories associated, pusher business, when youve made a deal
# and looking for pusher, when you havent met the pusher and tanktop asks if you know someone.
# You get up to times talked1 either having made the bussiness which happens automatically
# or being told its cool to make the deal, you can't go further if you don't know tanktop.


def pushertimes0content(player):
    if (
        "Looking for Pusher" in player.memories
        and "Pusher Business" not in player.memories
    ):
        print("You and your partner start casually talking to them")
        print("quickly confirming that, yes, they have some stuff to move around")
        print("")
        print("Your partner mentions some friends of a friend need a boost")
        print("")
        print("     You hook me up with a group and I'll give you a boost too")
        print("you say you might do just that")
        print("")
        player.NPCs["pusher"].times_talked = 1
        return True

    elif "Pusher Business" in player.memories:
        print("")
        print("     Thanks for the networking earlier.")
        print("     You're a cool cat. Here, for the trouble.")
        print("")
        sleep(3)
        print("the pusher gives you a pill and gives your partner some k ")
        print("your partner's beaming. you're both thankful.")
        player.items.append(items["special K"])
        player.memories.append("Commission")
        player.NPCs["partner"].kusesleft += 2
        player.NPCs["pusher"].times_talked = 1
        return True

    else:
        print("You make some polite small talk about how the party's going so far")
        print("the conversation doesn't go much further than that")
        return None
