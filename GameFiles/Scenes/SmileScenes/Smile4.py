# You've already met the pusher, this is sharing a moment, you get a memory, you need to dance with them to get to 5


def smiletimes4content(player):
    if player.location == player.rooms["dance floor"]:
        if player.party.music == "terrible":
            if player.NPCs["smile"].boost < 1.2:
                print("     I LOVE THIS SONG!!!")
                print("")
                print("And it shows. So much enthusiasm. No musical standards.")
                print("And you love that. It's infectious. It cheers you up.")
                print("")
                player.lit += 20
                player.NPCs["smile"].boost = 1.2
                return True

            if player.NPCs["smile"].boost >= 1.2:
                print("     Come on baby, I wanna see some moves from you too!")
                print("     Let's dance!")

        if player.party.music == "ok" or player.party.music == "great":
            print(
                "The smile ambassador is really into this particular song apparently."
            )
            print("The huge fan they're waving around seems a bit dangerous...")
            print("You're told, through body motion, to get your dance on too.")

    if player.location == player.rooms["smoking room"]:
        print("You talk a bit about how stuff is going for each of you.")
        print("     We gotta get our moves on tonight too! ")
        print("You consider maybe dancing a little later.")

    if player.location == player.rooms["bathroom"]:
        print("They're talking to someone else now, but they give you this look.")
        print("This we-gotta-go-dance look.")

    print("")
