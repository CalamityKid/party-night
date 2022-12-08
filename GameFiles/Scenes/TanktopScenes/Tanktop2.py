from time import sleep
from ...Input import yesorno

# One of their friends didn't bring candy, introduce them to the pusher if you can
def tanktoptimes2content(player):
    if player.location == player.rooms["dance floor"]:
        print("The cutie's busy talking to their group about something.")
        sleep(2)
        print("It's too loud in here to understand anything right now.")
        return None

    elif player.location != player.rooms["dance floor"]:
        print("You walk up to their group.")
        sleep(1)
        print("They're talking to each other about how to get candy")
        sleep(2)
        print("specifically they could use some pills.")
        print("")
        sleep(1)

        if player.NPCs["pusher"] in player.people_in_party:
            print("")
            print("     Do you wanna introduce them to your new pusher friend?")
            sleep(1)
            print("               It might take some time (y/n) ", end="")
            option = yesorno()
            if option == True:
                print("You look around the party for your new friend.")
                sleep(2)
                if player.party.crowd == "full":
                    player.time.ten_minutes()

                player.NPCs["pusher"].location = player.location
                player.location = player.NPCs["partner"].location
                player.location = player.NPCs["tanktop"].location

                print(
                    "You end up finding them in",
                    str(player.location.name),
                    "and you introduce them.",
                )
                sleep(2)
                print("Everybody seems pretty happy about the whole thing.")
                player.coolness += 30
                player.memories.append("Pusher Business")
                player.scenevariables.capeohour = player.time.hour
                player.scenevariables.capeominute = player.time.minute
                player.NPCs["tanktop"].times_talked = 3
                print("")
                return True

            elif option == False:
                print("You decide not to introduce them.")
                sleep(2)
                print("They ask you to please let them know if you hear about anyone.")
                player.memories.append("Looking for Pusher")
                player.NPCs["tanktop"].times_talked = 3
                print("")
                return None

        elif player.NPCs["pusher"] not in player.people_in_party:
            print("You tell them you don't know of anybody in here.")
            sleep(2)
            print("But you'll let them know if you hear anything.")
            player.memories.append("Looking for Pusher")
            player.NPCs["tanktop"].times_talked = 3
            print("")
            return None
