################################# Smile Borrow G
def smileborrowGcode():
    if "G" in player.active_items:
        print(
            """
	Baby, we already did some. Chill, you don't wanna drop on us.
	"""
        )

    if "G" not in player.active_items:
        if player.location != bathroom:
            print(
                """
	Yeah, for sure! Let's have some, baby!
	"""
            )
            if scenevariables.movementtimewarning == False:
                print(
                    """
	We'd have to go all the way to the bathroom, though.
    I don't wanna do the whole trip by myself.
    Especially when it's crowded. Takes forever. A nightmare.
    We can still go though. If you want...
	"""
                )
                scenevariables.movementtimewarning = True
            print(
                "You sure you wanna go all the way to the bathroom for this? (y/n)",
                end=" ",
            )
            option = yesorno()
            print("")
            if option == True:
                player.location = bathroom
                smile.location = bathroom
                if party.crowded == "crowded":
                    print(
                        "The smile ambassador and you slowly bump your way the crowd around to the bathroom."
                    )
                    time.ten_minutes()
                if party.crowded != "crowded":
                    print("You both find yourselves in the bathroom in no time.")
            if option == False:
                print(
                    """
	Alright, if you wanna go do tell me though.
	"""
                )

        if player.location == bathroom:
            if (
                smile.times_talked == 3
            ):  # This is if you havent met the pusher yet, similar to scene 3.
                print(
                    """
	Here they are! Remember I told you I wanted to introduce you to my friend?

Their friend is clearly a pusher. 
They seem nice.
You talk a bit, a lot of smiling on all parts."""
                )
                time.ten_minutes()
                people_in_party.append(pusher)
                smile.times_talked = 4

            if party.crowded == "crowded":
                if scenevariables.stalltimewarning == False:
                    print(
                        """
	It's pretty crowded in here.
    We're gonna have to wait a bit to get a stall."""
                    )
                    input()
                    print(
                        """
	It will probably take a while actually.
	"""
                    )
                    scenevariables.stalltimewarning = True
                print("You okay with waiting for a stall? (y/n)", end=" ")
                option = yesorno()
                if option == True:
                    print(
                        """
	Alright, let's do it.

It IS pretty crowded. Waiting. Small talk. 
After a few minutes a stall frees up.
You both get in."""
                    )
                    player.items["G"] = 40
                    player.use_item("G")
                    time.ten_minutes()
                if option == False:
                    print(
                        """
	Alright. Let me know if you change your mind."""
                    )

            if party.crowded != "crowded":
                print(
                    """
	Alright, let's do it!
	
and you go into an empty stall and do some G."""
                )
                player.items["G"] = 40
                player.use_item("G")


# smileborrowG = Scene("Smile Borrow G", smileborrowGcode)
