from ...Input import yesorno
from ...Scripts.Blocks import items

# already borrowed you know theyre leaving early and bitched about mad music, this is characterization and boost. Advance talking after 3 am.
def coupletimes3content(player):
    print("")
    if player.location == player.rooms["dance floor"]:
        print("They're both really enjoying themselves dancing.")
        return None
    elif player.location != player.rooms["dance floor"]:
        if player.party.music == "terrible":
            if player.time.hour < 3:
                print(
                    "You start talking to one of them about feminist theory and relativism"
                )
                print("the other one is smoking a blunt and looking placid as hell.")
                print("")
                if player.NPCs["couple"].boost < 1.2:
                    print("Youre really glad they're here with you tonight.")
                    player.NPCs["couple"].boost = 1.2
                    return True

            elif player.time.hour >= 3:
                print("Wow, the music's soooo bad, bitch!")
                print("says one of them")
                print(
                    "and the other one's nodding but doesn't really look very bothered."
                )
                print("")
                print("     And this DJ's gonna be playing til 5 too")
                print("     like all the time we're here basically, ugh.")
                print("Wow, the drama. But totally true though.")
                print("you feel their pain.")
                print("")
                if player.location == player.rooms["smoking room"]:
                    print("They also offer you a cigarrete.")
                    print("")
                    print("     Do you want a cigarrete? (y/n) ", end=" ")
                    option = yesorno()
                    if option == True:
                        print("You take the cigarette.")
                        player.items.append(items["cigarette"])
                    elif option == False:
                        print("You kindly turn down the offer.")
                player.NPCs["couple"].times_talked = 4
                return True

        elif player.party.music != "terrible":
            if "Changed Music" in player.memories:
                print("     Bitch, you really got the DJ to play something decent?!")
                print(
                    "says one of them while the other drops their cigarette to the floor."
                )
                print("")
                print("     You saved the night baby, love youu!")
                print("says one of them, while the other steps on the cigarette")
                print("and they both zip to the dance floor.")
                if player.NPCs["couple"].boost < 1.2:
                    print("")
                    print("You're looking forward to dancing with them.")
                    player.NPCs["couple"].boost = 1.2
                player.NPCs["couple"].times_talked = 4
                player.NPCs["couple"].location = player.rooms["dance floor"]
                return True
            elif "Changed Music" not in player.memories:
                print("     I heard the music got better, we should go dance!")
                print("says one of them while the other one is finishing a cigarette.")
                print("")
                print("     Yeah, bitch, let's get moving!")
                print("and they both make a beeline to the dance floor.")
                print("")
                player.NPCs["couple"].times_talked = 4
                player.NPCs["couple"].location = player.rooms["dance floor"]
                return True
