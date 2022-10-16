from time import sleep
from ...Scripts.Blocks import items
from ...Scripts.Actions import use_item
from ...Input import yesorno

################################# Smile Borrow G


def smileGcontent(player):
    print("")
    if items["G"] in player.active_items:
        print("          Baby, we already did some. Chill, you don't wanna drop on us.")
        print("")
        sleep(1)
        print("You DON'T wanna drop on them. Double dosing G is fucked up.")
        sleep(2)
        print("You decide to wait it out.")
        return None

    elif items["G"] not in player.active_items:
        if player.location != player.rooms["bathroom"]:
            print("     Yeah, for sure! Let's have some, baby!")

            if player.scenevariables.movementtimewarning == False:
                print("")
                print("      We'd have to go all the way to the bathroom, though.")
                sleep(1)
                print("      I don't wanna do the whole trip by myself.")
                sleep(1)
                print("      Especially when it's crowded. Takes forever. A nightmare.")
                sleep(2)
                print("      We can still go though. If you want...")
                sleep(1)
                print("")
                player.scenevariables.movementtimewarning = True
            print(
                "      You sure you wanna go all the way to the bathroom for this? (y/n)",
                end=" ",
            )
            option = yesorno()
            if option == True:
                player.location = player.rooms["bathroom"]
                player.NPCs["smile"].location = player.rooms["bathroom"]
                player.NPCs["partner"].location = player.rooms["bathroom"]
                if player.party.crowd == "full":
                    print("")
                    print(
                        "The smile ambassador and you slowly bump your way through the crowd."
                    )
                    sleep(1)
                    print("You finally make it to the bathroom.")
                    sleep(1)
                    player.time.ten_minutes()
                elif player.party.crowd != "full":
                    print("")
                    print("You both find yourselves in the bathroom in no time.")
            if option == False:
                print("")
                print("          Alright, if you wanna go do tell me though!")

        if player.location == player.rooms["bathroom"]:
            if (
                player.NPCs["smile"].times_talked == 3
            ):  # This is if you havent met the pusher yet, similar to scene 3.
                print("")
                print("     Look who's here! ", end="")
                sleep(2)
                print("Remember I told you I wanted to introduce you to my friend?")
                sleep(2)
                print("The smile ambassador introduces you to their friend.")
                sleep(1)
                print("Their friend is clearly a pusher.")
                sleep(2)
                print("They seem nice.")
                print("You end up talking a bit, there's smiling on both parts.")
                print("You kinda end up not doing any G.")
                player.people_in_party.append(player.NPCs["pusher"])
                player.NPCs["pusher"].location = player.rooms["bathroom"]
                player.NPCs["smile"].times_talked = 4
                return True

            if player.party.crowd == "full":
                if player.scenevariables.stalltimewarning == False:
                    print("")
                    print("      It's pretty crowded in here.")
                    print("      We're gonna have to wait a bit to get a stall.")
                    sleep(2)
                    print("      It will probably take a while actually.")
                    sleep(1)
                    print("")
                    player.scenevariables.stalltimewarning = True

                print("      You okay with waiting for a stall? (y/n)", end="")
                option = yesorno()
                if option == True:
                    print("      Alright, let's do it.")
                    print("")
                    sleep(1)
                    print("It IS pretty crowded. Waiting. Small talk.")
                    print("After a few minutes a stall frees up.")
                    print("You both get in.")
                    sleep(2)
                    player.items.append(items["G"])
                    use_item.execute(player, items["G"])
                    return True

                elif option == False:
                    print("      Alright. Let me know if you change your mind.")
                    print("")
                    return None

            if player.party.crowd != "full":
                print("      Alright, let's do it!")
                print("")
                sleep(1)
                print("and you go into an empty stall together")
                player.items.append(items["G"])
                use_item.execute(player, items["G"])
                return True
