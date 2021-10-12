##########################################SMILE SCENES
######################Smile Times1, offers G


def smiletimes1content(player):
    if player.location == player.rooms["bathroom"]:
        print("")
        print("The smile ambassador is scanning the room for hotties.")
        return None

    if player.location != player.rooms["bathroom"]:
        if player.location == player.rooms["dance floor"]:
            print("")
            print("Music's too loud to speak in here rn.")
            return None

        if player.location == player.rooms["smoking room"]:
            print("")
            print("     By the way, I got some G, babe, in case you want some later.")
            print("     We can't do it here in front of everyone though.")
            print("     So do consider we'd have to go to the bathroom to take it.")
            print("")  # Put a wait for input thingy here
            print(
                "     Yeah, it's a drag, especially when the party's packed, but it is what it is."
            )
            print("     So yeah, if you want some, just ask me for some whenever!")
            print("")
            player.NPCs["smile"].times_talked = 2
            return True
