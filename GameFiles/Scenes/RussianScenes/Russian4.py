from ...Input import yesorno

# You've already met the cutie, this is sharing a moment, it progresses to 5 when you make plans to go to a film festival


def russiantimes4content(player):
    if player.location == player.rooms["dance floor"]:
        if player.NPCs["russian"].boost >= 1.2:
            print("Music's really loud")
            print("so they just show you their phone")
            print("there's a film festival thing happening next week")
            print("you show your partner, and they nod")
            print("")
            print("     Do you wanna go to this music festival? (y/n) ", end="")
            option = yesorno()
            if option == True:
                print("You all agree to do that next week.")
                print("You're looking forward to it!")
                player.memories.append("Attending Film Festival")
            elif option == False:
                print("You turn down the offer.")
                print("Your partner looks a bit disappointed.")
                player.memories.append("Not Attending Festival")
            player.NPCs["russian"].times_talked = 5
            return True

        elif player.NPCs["russian"].boost < 1.2:
            print("     You liked my friend, riight?")
            print("     I thought you would!")
            print("like half screaming cause the music is loud af")
            print("and you answer but they don't really hear you")
            print(
                "they still do this thing where they nod just to end the conversation."
            )
            print("")
            print("You're just happy you get to party with your friend tonight.")
            print("")
            player.NPCs["russian"].boost = 1.2
            return True

    elif player.location == player.rooms["smoking room"]:
        print("     My friend, total cutie, huuh?")
        print("     I know you bitches and your tastes.")
        print("and your russian friend laughs like they always do")
        print("like somewhere between a chuckle and a snort.")
        print("")
        print("Your partner makes this licking their lips face.")
        print("     You in on that too? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("Yeah you're both looking forward to that.")
        elif option == False:
            print("You're not super into it.")
        print("")
        print("You all keep talking a bit longer ")
        print("you catch up on some stuff")
        print("end up getting invited to a film festival next weekend.")
        print("")
        print("     Do you wanna go to this music festival? (y/n) ", end="")
        option = yesorno()
        if option == True:
            print("You all agree to do that next week.")
            print("You're looking forward to it!")
            player.memories.append("Attending Film Festival")
        elif option == False:
            print("You turn down the offer.")
            print("Your partner looks a bit disappointed.")
            player.memories.append("Not Attending Film Festival")
        print("")
        print("You're happy you get to share with your friend tonight.")
        if player.NPCs["russian"].boost < 1.2:
            player.NPCs["russian"].boost = 1.2
        player.NPCs["russian"].times_talked = 5
        print("")
        return True

    elif player.location == player.rooms["bathroom"]:
        print("Your russian friend is so deep in flirting")
        print("with this like full leather clad kinkster")
        print("you decide not to bother them now.")
        return None
