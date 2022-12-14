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
        sleep(1)
        print("     I'll give you some more later if you want")
        print("")
        print("and that's that for now.")
        return None

    elif items["special K"] not in player.active_items:
        if player.NPCs["partner"].kusesleft == 0:
            print("")
            print("     I ran out, babe")
            sleep(1)
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
                sleep(2)
                print("")
                print("     But you can kill the bag now")
                print("")
                sleep(2)

            if player.location != player.rooms["bathroom"]:
                print("")
                print("     Yeah, I could use some freshening up!")
                sleep(2)
                print("your partner says half smiling")
                sleep(2)

            if player.scenevariables.movementtimewarning == False:
                print("")
                print("      We have to go to the bathroom then.")
                sleep(2)
                print("      It's a pain. Especially when it's crowded.")
                sleep(2)
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
                    sleep(2)
                    player.time.ten_minutes()

                elif player.party.crowd != "full":
                    print("")
                    print("You find yourselves in the bathroom in no time.")
                    sleep(2)

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
                        sleep(2)
                        print("     and there's a lot of people waiting.")
                        sleep(2)
                        print("     It takes a while when the party's this crowded.")
                        sleep(2)
                        print("      You want to wait? I don't mind...")
                        print("")
                        player.scenevariables.stalltimewarning = True

                    print("      You okay with waiting for a stall? (y/n)", end=" ")
                    option = yesorno()
                    if option == True:
                        print("      Alright babe, we wait.")
                        print("")
                        sleep(2)
                        print("And you wait like 10 minutes")
                        print("until a stall frees up.")
                        sleep(2)
                        print("You both get in.")
                        print("")
                        player.time.ten_minutes()
                        player.items.append(items["special K"])
                        use_item.execute(player, items["special K"])
                        player.NPCs["partner"].kusesleft -= 1
                        return True

                    if option == False:
                        print("")
                        print("     Okay love.")
                        print("     You tell me if you wanna try later.")
                        return None

                elif player.party.crowd != "full":
                    print("")
                    print("     Great, let's go!")
                    print("")
                    sleep(2)
                    print("you both go into the stall")
                    player.items.append(items["special K"])
                    use_item.execute(player, items["special K"])
                    player.NPCs["partner"].kusesleft -= 1
                    return True
