from time import sleep
from ...Input import yesorno
from ...Scripts.Blocks import items


# already borrowed you know theyre leaving early and bitched about mad music, this is characterization and boost. Advance talking after 3 am.
def coupletimes3content(player):
    print("")
    if player.time.hour < 3:
        print("You start talking to one of them about feminist theory and relativism")
        if player.location == player.rooms["smoking room"]:
            print("the other one is smoking a blunt and looking placid as hell.")
        else:
            print("the other one looks slightly stoned and placid as hell.")
        print("")
        sleep(2)
        if player.NPCs["couple"].boost < 1.2:
            print("You're really glad they're here with you tonight.")
            player.NPCs["couple"].boost = 1.2
            sleep(2)
        return None

    elif player.time.hour >= 3:
        if player.party.music == "terrible":
            print("")
            print("     Wow, the music's soooo bad, bitch!")
            sleep(2)
            print("says one of them")
            sleep(1)
            print("and the other one's nodding but doesn't really look very bothered.")
            print("")
            sleep(3)
            print("     And this DJ's gonna be playing til 5 too")
            sleep(2)
            print("     like all the time we're here basically, ugh.")
            sleep(3)
            print("")
            print("Wow, the drama. But totally true though.")
            sleep(2)
            print("you feel their pain.")
            print("")
            sleep(2)
            if player.location == player.rooms["smoking room"]:
                print("They also offer you a cigarrete.")
                print("")
                print("     Do you want a cigarrete? (y/n)", end=" ")
                option = yesorno()
                if option == True:
                    if items["cigarette"] in player.items:
                        print("You already have a cigarette.")
                    else:
                        print("You take the cigarette.")
                        player.items.append(items["cigarette"])
                elif option == False:
                    print("You kindly turn down the offer.")
                player.NPCs["couple"].times_talked = 4
            return True

        elif player.party.music != "terrible":
            if "Changed Music" in player.memories:
                print("     Bitch, you really got the DJ to play something decent!")
                sleep(2)
                print(
                    "says one of them while the other drops their cigarette to the floor."
                )
                sleep(2)
                print("")
                print("     You saved the night baby, love youu!")
                sleep(2)
                print("says one of them, while the other steps on the cigarette")
                sleep(2)
                print("")
                if player.NPCs["couple"].boost < 1.2:
                    print("You're looking forward to dancing with them.")
                    player.NPCs["couple"].boost = 1.2

                player.NPCs["couple"].times_talked = 4
                player.NPCs["couple"].location = player.rooms["dance floor"]
                print("")
                return True
            elif "Changed Music" not in player.memories:
                if player.location != player.rooms["dance floor"]:
                    print("     I heard the music got better, we should go dance!")
                    sleep(2)
                    print(
                        "says one of them while the other one is finishing a cigarette."
                    )
                    print("")
                    sleep(2)
                    print("     Yeah, bitch, let's get moving!")
                    sleep(1)
                    print("")
                    print("and they both make a beeline to the dance floor.")
                    print("")
                    sleep(2)
                    player.NPCs["couple"].location = player.rooms["dance floor"]
                else:
                    print("     The music's better! We should dance!")
                    sleep(2)
                    print("one of them says while the other is already dancing.")

                player.NPCs["couple"].times_talked = 4
                return True
