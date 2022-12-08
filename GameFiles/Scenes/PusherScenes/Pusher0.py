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
        sleep(2)
        print("quickly confirming that, ", end="")
        sleep(1)
        print("yes, ", end="")
        sleep(1)
        print("they have some stuff to move around")
        print("")
        sleep(1)
        print("Your partner mentions some friends of a friend need a boost")
        print("")
        sleep(2)
        print("     You hook me up with a group and I'll give you a boost too")
        sleep(2)
        print("")
        print("you say you might do just that")
        print("")
        player.NPCs["pusher"].times_talked = 1
        return True

    elif "Pusher Business" in player.memories:
        print("")
        print("     Thanks for the networking earlier.")
        sleep(1)
        print("     You're a cool cat. Here, for the trouble.")
        sleep(1)
        print("")
        print("the pusher gives you a pill and gives your partner some k ")
        sleep(1)
        print("your partner's beaming. you're both thankful.")
        player.items.append(items["special K"])
        player.memories.append("Commission")
        player.NPCs["partner"].kusesleft += 2
        player.NPCs["pusher"].times_talked = 1
        return True

    else:
        print("You make some polite small talk about how the party's going so far")
        sleep(1)
        print("the conversation doesn't go much further than that")
        return None
