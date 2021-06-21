from ...Scripts.Blocks import items
from ...Scripts.Actions import use_item
from ...Input import yesorno

################################# Smile Borrow G


def smileGcontent(player):
    print("")
    if items["G"] in player.active_items:
        print("          Baby, we already did some. Chill, you don't wanna drop on us.")
        print("")
        print("You DON'T wanna drop on them. Double dosing G is fucked up.")
        print("You decide to wait it out.")
        print("")
        return None

    elif items["G"] not in player.active_items:
        if player.location != player.rooms["bathroom"]:
            print("     Yeah, for sure! Let's have some, baby!")

            if player.scenevariables.movementtimewarning == False:
                print("")
                print("      We'd have to go all the way to the bathroom, though.")
                print("      I don't wanna do the whole trip by myself.")
                print("      Especially when it's crowded. Takes forever. A nightmare.")
                print("      We can still go though. If you want...")
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
                if player.party.crowd == "full":
                    print("")
                    print(
                        "The smile ambassador and you slowly bump your way through the crowd."
                    )
                    print("You finally make it to the bathroom.")
                    print("")
                    player.time.ten_minutes()
                if player.party.crowd != "full":
                    print("")
                    print("You both find yourselves in the bathroom in no time.")
                    print("")
            if option == False:
                print("")
                print("          Alright, if you wanna go do tell me though!")

        if player.location == player.rooms["bathroom"]:
            if (
                player.NPCs["smile"].times_talked == 3
            ):  # This is if you havent met the pusher yet, similar to scene 3.
                print("")
                print(
                    "     Look who's here! Remember I told you I wanted to introduce you to my friend?"
                )
                print("The smile ambassador introduces you to their friend.")
                print("Their friend is clearly a pusher.")
                print("They seem nice.")
                print("You end up talking a bit, there's smiling on both parts.")
                print("You kinda end up not doing any G.")
                print("")
                player.people_in_party.append(player.NPCs["pusher"])
                player.NPCs["pusher"].location = player.rooms["bathroom"]
                player.NPCs["smile"].times_talked = 4
                return True

            if player.party.crowd == "full":
                if player.scenevariables.stalltimewarning == False:
                    print("")
                    print("      It's pretty crowded in here.")
                    print("      We're gonna have to wait a bit to get a stall.")
                    print("")
                    print("      It will probably take a while actually.")
                    print("")
                    player.scenevariables.stalltimewarning = True

                print("      You okay with waiting for a stall? (y/n)", end="")
                option = yesorno()
                if option == True:
                    print("      Alright, let's do it.")
                    print("")
                    print("It IS pretty crowded. Waiting. Small talk.")
                    print("After a few minutes a stall frees up.")
                    print("You both get in.")
                    print("")
                    player.items.append(items["G"])
                    use_item.execute(player, items["G"])
                    return True

                elif option == False:
                    print("      Alright. Let me know if you change your mind.")
                    print("")
                    return None

            if player.party.crowd != "full":
                print("")
                print("      Alright, let's do it!")
                print("")
                print("and you go into an empty stall together")
                print("")
                player.items.append(items["G"])
                use_item.execute(player, items["G"])
                return True
