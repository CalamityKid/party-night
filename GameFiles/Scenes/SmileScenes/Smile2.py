from time import sleep

###################Smile times 2 #Tells you about introducing you to the pusher, skips to introducing him if conditions are right


def smiletimes2content(player):
    print("")
    if player.time.hour <= 2:
        print("     I wanted to introduce you to someone. ", end="")
        sleep(2)
        print("Who I get my candy from.")
        sleep(2)
        print("     I don't think they're still here yet.")
        sleep(2)
        print("     They'll probably be around later.")
        sleep(2)
        print("")
        print("You make a mental note of meeting this new ", end="")
        sleep(2)
        print("uh, ", end="")
        sleep(1)
        print("commercially inclined person.")
        player.NPCs["smile"].times_talked = 3
        print("")
        return True

    if player.time.hour > 2:
        if player.location == player.rooms["bathroom"]:
            print("          Hey babes, ", end="")
            sleep(1)
            print("I really wanted to introduce you guys.")
            sleep(2)
            print("")
            print("The smile ambassador introduces you two to their friend.")
            sleep(2)
            print("Their friend is clearly their pusher.")
            sleep(2)
            print("You two speak for a bit, ", end="")
            sleep(2)
            print("cool cat.")
            player.people_in_party.append(player.NPCs["pusher"])
            player.NPCs["pusher"].location = player.rooms["bathroom"]
            player.NPCs["smile"].times_talked = 4
            return True

        elif player.location != player.rooms["bathroom"]:
            print("")
            print("          I wanted to introduce you to my friend.")
            sleep(2)
            print("          They must be around here somewhere by now.")
            sleep(2)
            print("You agree to meet this friend when they show up later.")
            print("")
            player.NPCs["smile"].times_talked = 3
            return True
