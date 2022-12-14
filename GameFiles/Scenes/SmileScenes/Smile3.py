from time import sleep

# theyve already told you about introducing you, youre stuck here until you meet either here or in borrow
def smiletimes3content(player):
    print("")
    if player.location != player.rooms["dance floor"]:
        if player.time.hour >= 2:
            print("          Hey babes, ", end="")
            sleep(1)
            print("I wanted to introduce you guys.")
            sleep(2)
            print("")
            print("The smile ambassador introduces you two to their friend.")
            sleep(2)
            print("Their friend is clearly their pusher.")
            sleep(2)
            print("You two speak for a bit, ", end="")
            sleep(2)
            print("a lot of smiling on all parts.")
            player.people_in_party.append(player.NPCs["pusher"])
            player.NPCs["pusher"].location = player.location
            player.NPCs["smile"].times_talked = 4
            return True

        if player.time.hour < 2:
            print("They remind you they wanna introduce you to their friend later.")
            print("")

    elif player.location == player.rooms["dance floor"]:
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
                print("The smile ambassador is dancing up a storm, ", end="")
                sleep(2)
                print("using that huge ass fan as a prop.")
                sleep(2)
                print("You hear it opening and closing to the beat.")

                if "Tried Reaching Smile" in player.memories:
                    sleep(2)
                    print("Good luck trying to reach them like this.")
                    sleep(2)
                    print("Maybe another approach might work...")
                elif "Tried Reaching Smile" not in player.memories:
                    player.memories.append("Tried Reaching Smile")

        elif player.party.music != "terrible":
            print(
                "The smile ambassador is really into this particular song apparently."
            )
            sleep(3)
            print("The huge fan they're waving around seems a bit dangerous...")
