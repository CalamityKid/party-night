# capeo/eta moment could be added but im tired

from time import sleep


def partnergameovercontent(player):
    print("| _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ |")
    print("|/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \|")
    print("|\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/|")
    print("|/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \|")
    print("|\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/|")
    print("|                                                            |")
    print("|                                                            |")
    print("|                        Your partner                        |")
    print("|                  what a mess,", end=" ")
    sleep(2)
    print("just like you                |")
    sleep(2)
    print("|         you feel so lucky to have found each other.        |")
    print("|               Together, through thick and thin             |")
    print("|                                                            |")
    sleep(3)

    if "Too High" in player.memories:
        print("|      which is specially helpful when you fucking faint     |")
        sleep(2)
        if "Too High Twice" in player.memories:
            print("|                    twice in one night...                   |")
            sleep(2)
            print("|            you consider you might have a problem           |")
            sleep(2)
        print("|           you're still self conscious about that           |")
        sleep(2)
        print("|                                                            |")

    if "Partner Dance" in player.memories:
        print("|       You had a lot of fun on the dance floor together     |")
        print("|             and that's why you came out tonight!           |")
    elif "Partner Dance" not in player.memories:
        print("|     You didn't have that magic moment on the dance floor   |")
        print("|            tonight and you kinda hope you had...           |")

    print("|                                                            |")
    sleep(3)

    if "Changed Music" in player.memories:
        sleep(2)
        print("|      the crazy change-the-music plan thing worked too!     |")
        sleep(2)
        print("|                                                            |")

    if "Partner Link" in player.memories:
        print("|             You made time for each other tonight           |")
        print("|           and that alone makes the night worth it          |")

    elif "Partner Link" not in player.memories:
        print("|      You hope you had spent more quality time together     |")
        print("|            maybe make more time for each other             |")
    sleep(3)
    print("|                                                            |")

    if "Tanktop Interest" in player.memories:
        print("|    You had fun flirting with the cutie together tonight    |")
        if player.NPCs["tanktop"].flirt > 5:
            print("|                you hit it off pretty well too              |")
            print("|                    we'll see how it goes                   |")

    elif "Tanktop Partner" in player.memories:
        print("|     Your partner had their fun with the cutie tonight      |")
        if "Partner Hookup" in player.memories:
            print("|                   they really hit it off                   |")
            sleep(2)
            print("|                     you felt", end=" ")
            print(player.hookupfeeling)
        else:
            print("|               you're glad they had their fun               |")

    elif "Partner Conversation" in player.memories:
        print("|You and your partner have some talking to do|")
        print("|you've been avoiding a few conversations|")
        print("|about the nature of your relationship|")
        sleep(3)
        print("|and it seems like it's unavoidable now...|")
        sleep(2)

    print("|                                                            |")
    sleep(2)

    print("| _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ |")
    print("|/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \|")
    print("|\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/|")
    print("|/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \|")
    print("|\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/|")
