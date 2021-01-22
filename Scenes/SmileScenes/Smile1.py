##########################################SMILE SCENES
######################Smile Times1, offers G
def smiletimes1code(actor, player):
    if "[BORROW] something" not in player.location.available_actions:
        print("The smile ambassador is scanning the room for hotties.")

    if "[BORROW] something" in player.location.available_actions:
        if player.location == dance_floor:
            print("Music's too loud to speak in here.")

        if player.location != dance_floor:
            print(
                """
	By the way, I got some G, babe, in case you want some later.
	We can't do it here in front of everyone though.
	So do consider we'd have to go to the bathroom to take it."""
            )
            input()
            print(
                """
	Yeah, it's a drag, especially when the party's packed, but it is what it is. 
	So yeah, if you want some, just [BORROW] some from me whenever!"""
            )
            actor.items.append("G")
            actor.times_talked = 2


# SmileTimes1 = Scene("SmileTimes1", smiletimes1code)

################################### SmileTimes3