# theyve already told you about introducing you, youre stuck here until you meet either here or in borrow
def smiletimes3content(player):
    print("")
    if player.location == player.rooms["bathroom"]:
        if player.time >= 2:
            print("     Hey babe, I really wanted to introduce you to someone.")
            print("The smile ambassador introduces you to their friend.")
            print("Their friend is clearly a pusher. They seem nice.")
            print("You talk a bit, a lot of smiling on all parts.")
            player.people_in_party.append(player.NPCs["pusher"])
            player.NPCs["pusher"].location = player.rooms["bathroom"]
            player.NPCs["smile"].times_talked = 4
            return True
        if player.time < 2:
            print("They remind you they wanna introduce you to their friend later.")
            print("")

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
                print(
                    "The smile ambassador is dancing up a storm, using that huge ass fan as a prop."
                )
                print("You hear it opening and closing to the beat.")

        if player.party.music == "ok" or player.party.music == "great":
            print(
                "The smile ambassador is really into this particular song apparently."
            )
            print("The huge fan they're waving around seems a bit dangerous...")

    if player.location == player.rooms["smoking room"]:
        print("They remind you they wanna introduce you to their friend later.")
        print("")
