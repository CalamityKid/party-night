from ...Input import yesorno
from time import sleep

# Youre either looking for the pusher and stuck here or already introduced and have to wait for an hour to get to 4


def tanktoptimes3content(player):

    print("You walk up to the cutie in the tanktop.")
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
                print("but conversation ends up being about")
                print("what a great time they'd be having if their friend showed up.")
            elif "Tanktop Partner" in player.memories:
                print("You try to lift the mood up a bit")
                print("but conversation ends up being about")
                print("what a great time they'd be having if their friend showed up.")
            print("")
            sleep(2)
            return None

        elif player.NPCs["pusher"] in player.people_in_party:

            print("     Do you wanna introduce them to your pusher friend?")
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
                print("Everybody seems pretty happy about the whole thing.")
                player.coolness += 30
                player.memories.append("Pusher Business")
                player.scenevariables.capeohour = player.time.hour
                player.scenevariables.capeominute = player.time.minute
                print("")
                sleep(2)
                return True

            elif option == False:
                print("You decide not to introduce them.")
                print("They ask you to please let them know if you hear about anyone.")
                print("")
                sleep(2)
                return None

    elif "Pusher Business" in player.memories:
        print("     The saviors of the night!")
        print("")
        print("The cutie's friends are really happy with you two.")

        if "Tanktop Conversation" in player.memories:
            print("Your partner gives you this we're-missing-out look.")
            print("You're in for a talk after this for sure.")

        elif "Tanktop Interest" in player.memories:
            print("The cutie in the tanktop is in way better spirits")
            print("flirting game's back on point too")

        elif "Tanktop Conversation" in player.memories:
            print("Everybody's in better spirits")
            print("Your partner flirting is hitting home too")

        print("")
        sleep(2)

        ######################### Must be a full hour til the drugs kick in
        print("")

        hdif = player.time.hour - player.scenevariables.capeohour
        mdif = player.time.minute - player.scenevariables.capeominute
        if (hdif == 1 and mdif > 0) or hdif > 2:
            capeo = True
        else:
            capeo = False

        if capeo == True:
            print("They're all looking pretty lively. Looks like the candy kicked in.")
            player.NPCs["tanktop"].times_talked = 4
            print("")
            sleep(2)
            return None

        elif capeo == False:
            print("They're excited for the candy to kick in.")
            print("They're only talking about that atm.")
            print("")
            sleep(2)
            return None
