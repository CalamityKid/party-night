###################Smile times 2 #Tells you about introducing you to the pusher, skips to introducing him if conditions are right


def smiletimes2content(player):
    print("")
    if player.time.hour < 2:
        print("     I wanted to introduce you to someone. Who I get my candy from.")
        print("     I don't think they're still here yet.")
        print("     They'll probably be around later.")
        player.NPCs["smile"].times_talked = 3
        print("")
        return True

    if player.time.hour > 2:
        if player.location == player.rooms["bathroom"]:
            print("          Hey babe, I really wanted to introduce you to someone.")
            print("")
            print("The smile ambassador introduces you to their friend.")
            print("Their friend is clearly a pusher.")
            print("You two speak for a bit, cool cat.")
            player.people_in_party.append(player.NPCs["pusher"])
            player.NPCs["pusher"].location = player.rooms["bathroom"]
            player.NPCs["smile"].times_talked = 4
            return True

        elif player.location != player.rooms["bathroom"]:
            print("")
            print("          I wanted to introduce you my friend. My candy provider.")
            print("          They must be around here somewhere by now.")
            print("You agree to meet this friend when they show up later.")
            print("")
            player.NPCs["smile"].times_talked = 3
            return True
