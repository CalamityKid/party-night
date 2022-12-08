from time import sleep

# You've already met the pusher, this is sharing a moment, you get a memory, you need to dance with them to get to 5


def smiletimes4content(player):
    if player.location == player.rooms["dance floor"]:
        if player.party.music == "terrible":
            if player.NPCs["smile"].boost < 1.2:
                print("     I LOVE THIS SONG!!!")
                sleep(2)
                print("")
                print("And it shows. ", end="")
                sleep(2)
                print("So much enthusiasm. ", end="")
                sleep(2)
                print("No musical standards.")
                sleep(2)
                print("And you love that. ", end="")
                sleep(2)
                print("It's infectious. ", end="")
                sleep(2)
                print("It cheers you up.")
                print("")
                player.lit += 20
                player.NPCs["smile"].boost = 1.2
                return True

            elif player.NPCs["smile"].boost >= 1.2:
                print("     Come on baby, ", end="")
                sleep(2)
                print("I wanna see some moves from you too!")
                sleep(2)
                print("     Let's ", end="")
                sleep(2)
                print("dance!")
                return None

        elif player.party.music != "terrible":
            print(
                "The smile ambassador is really into this particular song apparently."
            )
            sleep(3)
            print("Their body language is all ", end="")
            sleep(2)
            print("come on get your dance on.")
            sleep(2)
            print("No words, just dance.")

    elif player.location == player.rooms["smoking room"]:
        print("You talk a bit about how stuff is going for each of you.")
        sleep(2)
        print("     We gotta get our moves on tonight too! ")
        sleep(2)
        print("You consider maybe dancing a little later.")

    elif player.location == player.rooms["bathroom"]:
        print("They're talking to someone else now, ", end="")
        sleep(2)
        print("but they give you this look.")
        sleep(2)
        print("You know that look.")
        sleep(2)
        print("It's the we-gotta-go-dance look.")
