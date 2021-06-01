###################Smile times 2 #Tells you about introducing you to the pusher, skips to introducing him if conditions are right


def smiletimes2code(actor, time, people_in_party, pusher):
    if time.hour < 2:
        print(
            """
	I wanted to introduce you to someone. Who I get my candy from.
	I don't think they're still here yet.
	They'll probably be around later."""
        )
        actor.times_talked = 3

    if time.hour > 2:
        if player.location == bathroom:
            print(
                """
	Hey babe, I really wanted to introduce you to someone.
	"""
            )
            print("The smile ambassador introduces you to their friend.")
            print("Their friend is clearly a pusher.")
            people_in_party.append(pusher)
            pusher.location = bathroom
            actor.times_talked = 4
            time.ten_minutes()

        if player.location != bathroom:
            print(
                """
	I wanted to introduce you to someone. Who I get my candy from.
	They must be around here somewhere."""
            )
            smile.times_talked = 3


# SmileTimes2 = Scene("SmileTimes2", smiletimes2code)