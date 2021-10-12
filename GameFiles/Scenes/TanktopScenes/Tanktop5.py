from ...Input import yesorno

# Already danced with them and have the boost. Get the Link and sex thing depending on the path (or your partner hooking up with them).
def tanktoptimes5content(player):
    if "Tanktop Link" not in player.memories:
        print("The cutie in the tanktop catches you looking and comes to you.")
        if player.location == player.rooms["dance floor"]:
            print("They take you to a more quiet spot.")

        print("")
        print("     You sweethearts have really made my night.")

        if "Tanktop Partner" in player.memories:
            print("     Especially you, sexy")
            print("they say to your partner with a wink")
            print("")
        print("     It's been very special.")
        print("     I hope we can keep hanging out.")
        print("you end up exchanging phone numbers and instantgram accounts")
        print("you speak a bit longer and go back to the dance floor.")
        print("")
        print("You're happy you met them and got to spend time together.")
        player.memories.append("Tanktop Link")
        return True

    elif "Tanktop Link" in player.memories:
        if "Tanktop Interest" in player.memories:
            if player.NPCs["tanktop"].flirt >= 10:
                print("You think they might wanna come home with you.")
                print("Maybe flirt one last time if you're up for that.")
                return None

            elif player.NPCs["tanktop"].flirt < 10:
                print("You think the cutie might wanna come home with you two tonight")
                print("They're really into flirting with you two.")
                print("Maybe keep that up?")
                return None

        elif "Tanktop Conversation" in player.memories:
            print("You've really made a connection with this cutie tonight.")
            print("Your partner's gonna want to talk about this back home for sure.")
            return None

        elif "Tanktop Partner" in player.memories:
            print("You've really made a connection with this cutie tonight.")
            if "Partner Hookup" not in player.memories:
                print("Your partner seems to be going all in this time.")
                print("They kinda eye you, like checking if you're okay with it.")
                print("")
                print(
                    "     Are you okay with your partner and the cutie in the tanktop"
                )
                print("               hooking up without you? (y/n) ", end="")
                option = yesorno()
                if option == True:
                    print(
                        "You signal you're cool with it and they're gone for a few minutes."
                    )
                    print("You keep doing your thing and after a bit they come back.")
                    print("They both seem pretty happy.")
                    print("You might ask your partner about it after the party's over.")
                    player.memories.append("Partner Hookup")
                    return True
                elif option == False:
                    print("You signal maybe not now.")
                    print("Your partner kinda eases on the flirting and lays back.")
                    return None

            elif "Partner Hookup" in player.memories:
                print("Your partner's even happier about it.")
                return None
