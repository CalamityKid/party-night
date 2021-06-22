from ...Input import yesorno

# PartnerTanktop0 should happen automatically if you go to a room where tanktop is not there and isnt dance floor


def partnertantoptimes0content(player):
    print("Now that the cutie's out of sight, your partner turns to you.")

    print("     So... the cutie in the tanktop.")
    print("     Hot, right?")
    print("basically asking you if you're on the same page.")
    option1 = None
    while option1 == None:
        print("")
        print("     Are you on the same page? (y/n) ", end="")
        option1 = yesorno()
        if option1 == True:
            print("     You'll say yes. That'd mean you'd both be trying, as a couple,")
            print("     to take the cutie in the tanktop home with you tonight.")
            print("                Are you sure? (y/n) ", end="")
            option2 = yesorno()
            if option2 == False:
                option1 = None
            elif option2 == True:
                print("You're like heck yeah let's go for it.")
                print("")
                print("     Yesss, I was hoping you'd say that.")
                print("     That'd be a good time, huh?")
                print("")
                print("Yes it would. Yes, it, would.")
                print("You get back to the partying.")
                player.memories.append("Tanktop Interest")
                return True

        elif option1 == False:
            print("     You'll say no. That'd mean you're not interested in trying")
            print("      to take the cutie in the tanktop home with you tonight.")
            print("                 Are you sure? (y/n) ", end="")
            option2 = yesorno()
            if option2 == False:
                option1 = None
            elif option2 == True:
                print("You're like no, not interested.")
                print("")
                print("     Ah, I was hoping you were into the idea.")
                print("kinda disappointed sounding")
                print("and after a few seconds")
                print("")
                print("     Uh, do you mind if I go for it by myself?")
                print("")
                option3 = None
                while option3 == None:
                    print("     Do you mind? (y/n) ", end="")
                    option3 = yesorno()
                    if option3 == True:
                        print(
                            "      You'll say you do mind. That'd mean you wouldn't be okay"
                        )
                        print(
                            "     with your partner pursuing the cutie in the tanktop tonight."
                        )
                        print("              Are you sure? (y/n) ", end="")
                        option4 = yesorno()
                        if option4 == False:
                            option3 = None
                        elif option4 == True:
                            print(
                                "You say, you do, in fact, mind. And you'd prefer it if they didn't."
                            )
                            print("")
                            print(
                                "     Huh. Okay. I guess we'll talk about it when we get home..."
                            )
                            print("")
                            print(
                                "That tone of voice. You're in for a discussion later on..."
                            )
                            print("You get back to the partying.")
                            player.memories.append("Tanktop Conversation")
                            return True

                    elif option3 == False:
                        print(
                            "      You'll say you don't mind. That'd mean you'd be be okay with"
                        )
                        print(
                            "     your partner trying to pursue the cutie in the tanktop tonight."
                        )
                        print("              Are you sure? (y/n) ", end="")
                        option4 = yesorno()
                        if option4 == False:
                            option3 = None
                        elif option4 == True:
                            print(
                                "You say, you don't mind. YOu give your partner your blessing."
                            )
                            print("")
                            print("     Alright! Wish me luck!")
                            print("and you get back to the partying.")
                            player.memories.append("Tanktop Partner")
                            return True
