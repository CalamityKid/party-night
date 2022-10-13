from time import sleep
from ...Input import yesorno
from ...Scripts.Blocks.ItemsSc import items
from ...Scripts.Actions import use_item


# Youve met tanktop and talked to pusher after, you might or might not have your commission.


def pushertimes1content(player):

    if "Comission" in player.memories:
        if (
            items["blunt"] not in player.active_items
            and player.location.name == "the smoking room"
        ):
            print("they're smoking some green")
            print("     Heyy! yes. The cool cats!")
            print("you talk a little. They offer some weed.")
            print("")
            print("     Do you want a puff? (y/n)", end=" ")
            op = yesorno()
            if op == True:
                print("")
                print("You say yes, thankyouverymuch.")
                sleepp(2)
                player.items.append(items["blunt"])
                use_item.execute(player, items["blunt"])
                print("")
                print("you thank them and then tal a bit longer.")
                sleep(1)
                return True

            elif op == False:
                print("You kindly refuse.")
                print("")
                sleep(2)
                print("     You just let me know, my spliff's your spliff.")
                print("     Have a good one.")
                sleep(2)
                return None

        else:  # the default if conditions arent met and you got the commision already
            print("")
            print("     Enjoying yourselves tonight?")
            print("all friendly like, super articulate.")
            sleep(2)
            print("you chatter on for a bit before going back to the party.")
            return None

    elif (
        "Looking for Pusher" in player.memories
        and "Pusher Business" not in player.memories
    ):
        print("but instead you consider you could")
        print("go talk to the cutie in the tanktop and play matchmaker instead.")
        return None

    elif "Pusher Business" in player.memories and "Commission" not in player.memories:
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
        return True

    else:
        print("you idly talk about not much at all")
        sleep(1)
        return None
