from ...Scripts.Format.FlirtCalculations import flirting
from ...Input import yesorno
from time import sleep


def tanktopflirtcontent(player_obj):
    if player_obj.NPCs["tanktop"].times_talked == 0:
        print("Maybe test the waters first?")
        return None

    ###In these situations you cannot flirt with this character
    elif player_obj.NPCs["tanktop"].times_talked >= 1:
        if (
            "Tanktop Conversation" not in player_obj.memories
            and "Tanktop Interest" not in player_obj.memories
            and "Tanktop Partner" not in player_obj.memories
        ):
            print("You consider talking to your partner before making a move.")
            return None
        elif (
            "Tanktop Conversation" in player_obj.memories
            or "Tanktop Partner" in player_obj.memories
        ):
            print("You've decided you're gonna sit this one out.")
            return None
    ###In these situations you cannot flirt with this character

    # Flirting allowed, get Tanktop Interest memory in PartnerTanktop Scene that plays automaically in Schedule.
    # Levels are capped depending on times talked
    if "Tanktop Interest" in player_obj.memories:
        if player_obj.NPCs["tanktop"].times_talked == 1:
            print("You consider maybe talking a little more first.")
            return None

        if (
            player_obj.NPCs["tanktop"].times_talked >= 2
        ):  # you can actually flirt. Levels are capped depending on times talked.

            if player_obj.NPCs["tanktop"].times_talked == 2:  # CAPS TIMES TALKED 2
                if player_obj.NPCs["tanktop"].flirt >= 4:
                    print(
                        "They seem to be distracted talking with their friends about something."
                    )
                    return None

            elif player_obj.NPCs["tanktop"].times_talked == 3:  # CAPS TIMES TALKED 3
                if player_obj.NPCs["tanktop"].flirt > 6:
                    if "Pusher Business" in player_obj.memories:
                        if player_obj.NPCs["tanktop"].flirt > 8:
                            print("Looks like they want to dance.")
                            return None

                    elif "Looking for Pusher" in player_obj.memories:
                        print(
                            "You don't get through, they're focused on their shortage problem."
                        )
                        return None

                    elif "Looking for Pusher" not in player_obj.memories:
                        print("Seems like something's going on with their friends.")
                        print("Maybe talk to them about it.")
                        return None

            elif player_obj.NPCs["tanktop"].times_talked == 4:  # CAPS TIMES TALKED 4
                if player_obj.NPCs["tanktop"].flirt > 8:
                    print("Looks like they want to dance.")
                    return None

            # TIMES TALKED 5. NO CAPS, but possible ENDGAME.
            elif player_obj.NPCs["tanktop"].times_talked == 5:
                if player_obj.NPCs["tanktop"].flirt > 10:

                    if "Tanktop Asks" not in player_obj.memories:
                        print("Your partner's all over them")
                        print("and they look so hot together.")
                        sleep(2)
                        print("They lust for you too.")
                        sleep(2)
                        print("They want you all to go home and play")
                        sleep(2)

                        player_obj.memories.append("Tanktop Asks")

                    if "Tanktop Asks" in player_obj.memories:
                        op = None
                        op2 = None
                        print(
                            "     Do you want to leave the party with the cutie in the tanktop? (y/n)",
                            end=" ",
                        )
                        op = yesorno()

                        if op == True:
                            print("")
                            print(
                                "     This would end the night. Are you sure? (y/n)",
                                end=" ",
                            )
                            op2 = yesorno()
                            if op2 == True:
                                print("")
                                print("You look at them and unwillingly smile")
                                sleep(1)
                                print("a smile like someone about to misbehave")
                                sleep(1)
                                print("a smile of hunger and excitement")
                                sleep(2)
                                print("you signal to your friends and you all go home.")
                                player_obj.time.narrate()
                                player_obj.memories.append("Tanktop Home")
                                player_obj.gameover = True
                                return None

                        if op == False or op2 == False:
                            print("You tell them to wait a little longer. ")
                            return None

    ######if you havent run into a capped Return statement this is where the magic happens

    flirting_result = flirting(player_obj)
    if flirting_result == True:
        player_obj.modify_stat("lit", 10, True)
        player_obj.NPCs["tanktop"].flirt += 1

    elif flirting_result == True:
        player_obj.modify_stat("lit", 10, False)
        player_obj.NPCs["tanktop"].flirt += 1

    return True
