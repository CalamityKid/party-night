from time import sleep
from ...Input import yesorno

# plays if coolness > 60 and it hasnt played yet


def partneranxietycontent(player):
    print("Your partner side-eyes you for a moment")
    print("then puts a hand on your shoulder and pulls you to the side")
    print("     Are you okay babe?")
    print("     You seem tense.")
    print("")
    print("You do feel tense. You feel like people are looking at you.")
    print("You like the attention but it's making you very self aware.")
    sleep(3)
    print("")

    print("     Just focus on us, let's hang with our friends.")
    print("     If you wanna leave, we can leave anytime babe.")
    print("     Try not to mind the other people.")
    print("     You just say the word, okay? ")
    print("")
    print("          okay? (y/n)", end="")
    option = yesorno()

    if option == True:
        print("you nod")
        print("")
        print("     Alright love, let's have fun. ")
        print("and you feel more calm, more backed up.")

    elif option == False:
        print("you shake your head")
        print("you hate that you get like this")
        print("     Baby, this is about you, not about them.")
        print(
            "     You don't even know these people, it doesn't matter what they think."
        )
        print("     You're here for yourself.")
        print("     And if you wanna leave, we leave, it's fine.")
        sleep(4)
        print("and that's true of course.", end=" ")
        sleep(2)
        print("Of course.")
        sleep(1)
        print("you breathe a bit and do your whole mindfulness bs.")
        print("it calms you down a bit.")

    player.modify_stat("coolness", False, 30)
    return False