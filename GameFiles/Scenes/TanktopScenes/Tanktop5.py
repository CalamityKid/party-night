from time import sleep
from ..PartnerScenes.Compile import partnerscenes


# Already danced with them and have the boost. Get the Link and sex thing depending on the path (or your partner hooking up with them).
def tanktoptimes5content(player):
    if "Tanktop Link" not in player.memories:
        print("The cutie in the tanktop catches you looking and comes to you.")
        sleep(2)
        if player.location == player.rooms["dance floor"]:
            print("They take you to a more quiet spot.")
            sleep(2)

        print("")
        print("     You sweethearts have really made my night.")
        sleep(2)

        if "Tanktop Partner" in player.memories:
            print("     Especially you, sexy")
            sleep(2)
            print("while looking at your partner and smiling")
            sleep(2)
            print("")
        print("     It's been very special.")
        sleep(2)
        print("     I hope we can keep hanging out.")
        sleep(2)
        print("")
        print("you end up exchanging phone numbers and instantgram accounts")
        sleep(2)
        print("you speak a bit longer and go back to the dance floor.")
        sleep(2)
        print("")
        print("You're happy you met them and got to spend time together.")
        sleep(2)
        player.memories.append("Tanktop Link")
        return True

    elif "Tanktop Link" in player.memories:
        if "Tanktop Interest" in player.memories:
            if player.NPCs["tanktop"].flirt >= 10:
                print("You think they might wanna come home with you.")
                sleep(2)
                print("Maybe flirt one last time if you're up for that.")
                return None

            elif player.NPCs["tanktop"].flirt < 10:
                print("You think the cutie might wanna come home with you two tonight")
                sleep(2)
                print("They're really into flirting with you two.")
                sleep(2)
                print("Maybe keep that up?")
                return None

        elif "Tanktop Conversation" in player.memories:
            print("You've really made a connection with this cutie tonight.")
            sleep(2)
            print("Your partner's gonna want to talk about this back home for sure.")
            return None

        elif "Tanktop Partner" in player.memories:
            print("You've really made a connection with this cutie tonight.")
            if "Partner Hookup" not in player.memories:
                print("")
                return partnerscenes["PartnerTanktop5"].run_scene(player)

            elif "Partner Hookup" in player.memories:
                print("Your partner's even happier about it.")
                return None
