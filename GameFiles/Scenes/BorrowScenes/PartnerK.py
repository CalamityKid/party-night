from time import sleep
from ...Scripts.Blocks import items
from ...Scripts.Actions import use_item
from ...Input import yesorno

# the default is 3 uses, in the character setup. If you get the comission from the pusher you get 2 more.


def partnerkcontent(player):
    print("you ask your partner for some k")
    if items["special K"] in player.active_items:
        print("")
        print("     You just did some, babe")
        print("     I'll give you some more later if you want")
        print("and that's that for now.")
        sleep(2)
        return None

    elif items["special K"] not in player.active_items:
        if player.NPCs["partner"].kusesleft == 0:
            print("")
            print("     I ran out, babe")
            print("     I'm sorry")
            print("")
            sleep(2)
            print("and it's genuine sadness")
            print("you almost feel bad for asking")
            sleep(2)
            return None

        elif player.NPCs["partner"].kusesleft > 0:

            if player.NPCs["partner"].kusesleft == 1:
                print(
                    "your partner tells you they just gave some to your russian friend"
                )
                print("     But you can kill the bag now")
                print("")

            if player.location != player.rooms["bathroom"]:
                print("")
                print("     Yeah, I could use some freshening up!")
                print("your partner says half smiling")

            if player.scenevariables.movementtimewarning == False:
                print("")
                print("      We have to go to the bathroom then.")
                print("      It's a pain. Especially when it's crowded.")
                print("      But you gotta do what you gotta do.")
                print("")
                sleep(2)
                player.scenevariables.movementtimewarning = True
            print(
                "      You really wanna go all the way to the bathroom for this? (y/n)",
                end=" ",
            )
            option = yesorno()
            if option == True:

                if player.party.crowd == "full":
                    print("")
                    print("Your partner and you slowly make your way to the bathroom.")
                    player.time.ten_minutes()

                elif player.party.crowd != "full":
                    print("")
                    print("You both find yourselves in the bathroom in no time.")
                    print("")

                player.location = player.rooms["bathroom"]
                player.NPCs["partner"].location = player.rooms["bathroom"]

            if option == False:
                print("")
                print("          Okay babe, let me know if you change your mind.")
                sleep(2)
                return None

            if player.location == player.rooms["bathroom"]:
                if player.party.crowd == "full":
                    if player.scenevariables.stalltimewarning == False:
                        print("")
                        print("     We're gonna need to go into a stall")
                        print("     and there's a lot of people waiting.")
                        print("     It takes a while when the party's this crowded.")
                        print("      You want to wait? I don't mind...")
                        print("")
                        player.scenevariables.stalltimewarning = True

                    print("      You okay with waiting for a stall? (y/n)", end=" ")
                    option = yesorno()
                    if option == True:
                        print("      Alright babe, we wait.")
                        print("")
                        print("And you wait like 10 minutes")
                        print("until a stall frees up.")
                        print("You both get in.")
                        print("")
                        player.time.ten_minutes()
                        player.items.append(items["special K"])
                        use_item.execute(player, items["special K"])
                        player.NPCs["partner"].kusesleft -= 1
                        sleep(2)
                        return True

                    if option == False:
                        print("")
                        print("     Okay love.")
                        print("     You tell me if you wanna try later.")
                        sleep(2)
                        return None

                elif player.party.crowd != "full":
                    print("")
                    print("     Great, let's go!")
                    print("")
                    print("you both go into the stall")
                    player.items.append(items["special K"])
                    use_item.execute(player, items["special K"])
                    player.NPCs["partner"].kusesleft -= 1
                    sleep(2)
                    return True
