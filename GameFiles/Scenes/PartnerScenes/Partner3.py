from .Compile import partnerscenes

# in order to get here, you have to dance after boost is more than 1.3
# if between 3.30 and 5, it returns PartnerGather0.  To get to times 4 has to be before 5 am.


def partnertimes3content(player):
    if (
        player.time.hour >= 5 or "Music Changed" in player.memories
    ):  # gather scene finished
        if player.NPCs["partner"].boost < 1.4:
            print("     It was a fun plan")
            print("     but it was a bit silly.")
            print("")
            print("you let out a chuckle")
            print("it really was silly")
            print("")
            if "Music Changed" not in player.memories:
                print("     I'm glad we at least thought about it")
            elif "Music Changed" in player.memories:
                print("     and we managed to pull it off!")
                print("     just ridiculous")
                print("     I'm glad we thought about it")
            print("")
            print("and so are you, you'll remember this later")

            if "Music Changed" not in player.memories:
                print("it was dumb, but fun")

            print("and you consider")
            print("this is why you've been together this long")
            player.modify_stat("lit", 10, True)
            player.NPCs["partner"].boost = 1.4
            return True

        elif player.NPCs["partner"].boost == 1.4:
            player.NPCs["partner"].times_talked = 4
            return partnerscenes["Times4"].run_scene(player)

        else:
            return partnerscenes["Gather0"].run_scene(player)
