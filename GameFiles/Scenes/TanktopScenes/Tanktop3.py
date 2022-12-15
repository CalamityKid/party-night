from ...Input import yesorno
from time import sleep

# Youre either looking for the pusher and stuck here or already introduced and have to wait for an hour to get to 4


def tanktoptimes3content(player):

    if (
        "Looking for Pusher" in player.memories
        and "Pusher Business" not in player.memories
    ):

        if player.NPCs["pusher"] not in player.people_in_party:
            print("The whole group's morale is pretty low.")

            if "Tanktop Conversation" in player.memories:
                print("Maybe you should try to get them a contact.")

            elif "Tanktop Interest" in player.memories:
                print("You try to lift the mood up a bit")
                sleep(1)
                print("but conversation ends up being about")
                sleep(1)
                print("what a great time they'd be having if their friend showed up.")

            elif "Tanktop Partner" in player.memories:
                print("You try to lift the mood up a bit")
                sleep(1)
                print("but conversation ends up being about")
                sleep(1)
                print("what a great time they'd be having if their friend showed up.")
            print("")
            return None

        elif player.NPCs["pusher"] in player.people_in_party:

            print("     Do you wanna introduce them to your pusher friend?")
            sleep(1)
            print("               It might take some time (y/n) ", end="")
            option = yesorno()
            if option == True:
                print("You look around the party for your new friend.")
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
                sleep(1)
                print("Everybody seems pretty happy about the whole thing.")
                player.coolness -= 30
                player.memories.append("Pusher Business")
                player.scenevariables.capeohour = player.time.hour
                player.scenevariables.capeominute = player.time.minute
                print("")
                return True

            elif option == False:
                print("You decide not to introduce them.")
                sleep(1)
                print("They ask you to please let them know if you hear about anyone.")
                print("")
                return None

    elif "Pusher Business" in player.memories:
        if "Saviors" not in player.memories:
            print("")
            print("     The saviors of the night!")
            print("")
            sleep(2)
            print("The cutie's friends are really happy with you two.")
            sleep(2)

            if "Tanktop Conversation" in player.memories:
                print("Your partner gives you this we're-missing-out look.")
                sleep(2)
                print("You're in for a talk after this for sure.")

            elif "Tanktop Interest" in player.memories:
                print("The cutie in the tanktop is in way better spirits")
                sleep(2)
                print("flirting game's back on point too")

            elif "Tanktop Conversation" in player.memories:
                print("Everybody's in better spirits")
                sleep(2)
                print("Your partner flirting is hitting home too")
            player.memories.append("Saviors")
            print("")
            sleep(2)

        ######################### Must be 30 minutes for the drugs to kick in
        print("")

        capt = (
            player.scenevariables.capeohour * 60
        ) + player.scenevariables.capeominute
        currt = (player.time.hour * 60) + player.time.minute
        dif = currt - capt
        if dif >= 30:
            capeo = True
        else:
            capeo = False

        if capeo == True:
            print("They're all looking pretty lively. Looks like the candy kicked in.")
            player.NPCs["tanktop"].times_talked = 4
            print("")
            return None

        elif capeo == False:
            print("They're excited for the candy to kick in.")
            sleep(2)
            print("They're only talking about that atm.")
            sleep(2)
            print("")
            return None
