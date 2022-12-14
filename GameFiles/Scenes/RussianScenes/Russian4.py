from ...Input import yesorno
from time import sleep

# You've already met the cutie, this is sharing a moment, it progresses to 5 when you make plans to go to a film festival


def russiantimes4content(player):
    if player.location == player.rooms["dance floor"]:
        if player.NPCs["russian"].boost >= 1.2:
            print("Music's really loud")
            sleep(2)
            print("so they just show you their phone")
            sleep(2)
            print("there's a film festival thing happening next week")
            sleep(2)
            print("you show your partner, and they nod")
            print("")
            print("     Do you wanna go to this music festival? (y/n) ", end="")
            option = yesorno()
            if option == True:
                print("You all agree to do that next week.")
                sleep(2)
                print("You're looking forward to it!")
                player.memories.append("Attending Film Festival")
            elif option == False:
                print("You turn down the offer.")
                sleep(2)
                print("Your partner looks a bit disappointed.")
                player.memories.append("Not Attending Festival")
            player.NPCs["russian"].times_talked = 5
            return True

        elif player.NPCs["russian"].boost < 1.2:
            print("     You liked my friend, riight?")
            sleep(2)
            print("     I thought you would!")
            sleep(2)
            print("")
            print("like half screaming cause the music is loud af")
            sleep(2)
            print("and you answer but they don't really hear you")
            sleep(2)
            print(
                "they still do this thing where they nod just to end the conversation."
            )
            sleep(2)
            print("")
            print("You're happy you get to party with your friend tonight.")
            print("It had been a while.")
            player.NPCs["russian"].boost = 1.2
            return True

    elif player.location == player.rooms["smoking room"]:
        print("     My friend, total cutie, huuh?")
        sleep(2)
        print("     I know you bitches and your tastes.")
        sleep(2)
        print("")
        print("and your russian friend laughs like they always do")
        print("like somewhere between a chuckle and a snort.")
        print("")
        sleep(2)
        print("Your partner makes this licking their lips face.")
        print("     You in on that too? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("Yeah you're both looking forward to that.")
        elif option == False:
            print("You're not super into it.")
        print("")
        sleep(2)
        print("You all keep talking a bit longer ")
        sleep(2)
        print("you catch up on some stuff")
        print("end up getting invited to a film festival next weekend.")
        print("")
        sleep(2)
        print("     Do you wanna go to this music festival? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You all agree to do that next week.")
            sleep(2)
            print("You're looking forward to it!")
            player.memories.append("Attending Film Festival")
        elif option == False:
            print("You turn down the offer.")
            sleep(2)
            print("Your partner looks a bit disappointed.")
            player.memories.append("Not Attending Film Festival")
        print("")
        print("You're happy you get to share with your friend tonight.")
        sleep(2)
        print("It had been a while.")
        if player.NPCs["russian"].boost < 1.2:
            player.NPCs["russian"].boost = 1.2
        player.NPCs["russian"].times_talked = 5
        return True

    elif player.location == player.rooms["bathroom"]:
        print("Your russian friend is so deep in flirting")
        print("with this like", end="")
        sleep(1)
        print(" full leather clad kinkster")
        sleep(2)
        print("you decide not to bother them now.")
        sleep(2)
        return None
