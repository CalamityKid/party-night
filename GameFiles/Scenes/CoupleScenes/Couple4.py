from ...Input import yesorno


# its after 3 am, they bitched about the DJ and you MAYBE changed the music, maybe didn't. Advance by dancing with them, dance gives you dance memory. If music is terrible you can convince them to come down anyway.


def coupletimes4content(player):
    print("")
    if player.location == player.rooms["dance floor"]:
        if "Changed Music" in player.memories:
            print(
                "They are so glad you changed the music, they're dancing their hearts out."
            )
            if player.NPCs["couple"].boost < 1.2:
                print("Youre really glad they're here with you tonight.")
                player.NPCs["couple"].boost = 1.2
            return None
        elif player.party.music == "terrible":
            print(
                "One of them is moving to the music, the other one is cringing and looking around."
            )
            return None

    elif player.location != player.rooms["dance floor"]:
        if player.party.music == "terrible":
            print("One of them's really not into dancing to this music.")
            print("You can tell the other one's more open to it...")
            print("")
            print("It might take some time...")
            print("but you think you might talk them into going to the dance floor.")
            print("     Do you wanna try? (y/n) ", end="")
            option = yesorno()
            if option == True:
                print(
                    "You remind one of them about other times the music's been pretty terrible"
                )
                print("and you still ended up having a good time despite of it")
                print("the other one joins your efforts")
                print("your partner also helps.")
                print("")
                print(
                    "Finally your efforts pay off and you all decide to come down to the dance floor."
                )
                player.time.ten_minutes()
                player.location = player.rooms["dance floor"]
                player.NPCs["partner"].location = player.rooms["dance floor"]
                player.NPCs["couple"].location = player.rooms["dance floor"]
                player.memories.append("Couple Convinced")

                return True

            elif option == False:
                print("")
                print("You decide against it.")
        elif player.party.music != "terrible":
            ######################
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
                player.NPCs["couple"].location = player.rooms["dance floor"]
                print("")
                return True

            elif "Changed Music" not in player.memories:
                print("     I heard the music got better, we should go dance!")
                print("says one of them while the other one is finishing a cigarette.")
                print("")
                print("     Yeah, bitch, let's get moving!")
                print("and they both make a beeline to the dance floor.")
                print("")
                player.NPCs["couple"].location = player.rooms["dance floor"]
                return True
