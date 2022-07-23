from ...Input import yesorno
from ...Scripts.Format.formatting import format_objects_string
from ...Scripts.Format.Calculations import not_on_dance_floor

# you have either Gathering or Not Gathering in memories, gotten in partnergather0
# either get everybody and dance and change the music


def partnergather1content(player):
    if "Not Gathering" in player.memories:
        print("Music's still pretty bad")
        print("this DJs up til 5 am")
        print("you hold your head with one hand ")
        print("and look over at your partner, who's mouthing")
        print("     You want us to do the whole gather everyone thing? (y/n)", end=" ")

        option = yesorno()
        if option == True:
            print("")
            print("you say yeah, I guess")
            print("and it's time to look for your friends.")
            player.memories.append("Gathering")
            player.memories.remove("Not Gathering")
            return False

        elif option == False:

            print("you say nah, not worth it and wave it off")
            return False

    elif "Gathering" in player.memories:
        notondancefloorlist = not_on_dance_floor(player)

        print("your partner tells you")
        print("")

        if len(notondancefloorlist) != 0:
            notondancefloorstring = format_objects_string(notondancefloorlist)
            liststring = (
                "     We still have to get "
                + str(notondancefloorstring[:-1])
                + " on board."
            )
            print("you agree")
            print("you should find them and talk to them.")
            print("")
            return False

        elif len(notondancefloorlist) == 0:
            print("     I guess everybody's on the dance floor")
            print("     Let's go dance!")
            print("")
            print("and you're hoping this works")
            print("cause you cannot stand this music anymore")
            return False
