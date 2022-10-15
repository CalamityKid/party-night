from .Scripts.Blocks.PlayerSc import player
from .Scenes.CoupleScenes.Compile import couplescenes
from .Scenes.PartnerScenes.Compile import partnerscenes
from .Scenes.TanktopScenes.Compile import tanktopscenes
from .Scenes.PartnerScenes.Compile import partnerscenes


def update_schedule():
    ################ CROWDS #############
    if player.time.hour < 1 or player.time.hour >= 5:
        player.party.change_crowd_empty()
    elif player.time.hour == 1 or player.time.hour == 4:
        player.party.change_crowd_half()
    elif player.time.hour == 2 or player.time.hour == 3:
        player.party.change_crowd_full()

    ################## Music ############# Must get the exception of the cutscne thingy
    if player.time.hour < 1 or player.time.hour == 2:
        player.party.change_music_ok()

    elif player.time.hour == 1 or player.time.hour == 3:
        if "Changed Music" not in player.memories:
            player.party.change_music_terrible()
        elif "Changed Music" in player.memories:
            player.party.change_music_great()

    elif player.time.hour >= 5:
        player.party.change_music_great()

    ######### characters moving around and player.timeD events ###############
    if player.time.hour == 0 and player.time.minute == 00:
        player.NPCs["smile"].location = player.rooms["smoking room"]
        player.NPCs["russian"].location = player.rooms["smoking room"]
    if player.time.hour == 0 and player.time.minute == 30:
        player.NPCs["smile"].location = player.rooms["bathroom"]
        player.NPCs["russian"].location = player.location
        couplescenes["Times0"].run_scene(player)  # runs couple times 0 when its 00.30
        player.time.ten_minutes()

    if player.time.hour == 1 and player.time.minute == 00:
        player.NPCs["russian"].location = player.rooms["dance floor"]
        player.NPCs["smile"].location = player.rooms["smoking room"]
        player.NPCs["couple"].location = player.rooms["smoking room"]

    if player.time.hour == 1 and player.time.minute == 30:
        player.NPCs["couple"].location = player.rooms["smoking room"]
        player.NPCs["russian"].location = player.rooms["bathroom"]
        player.NPCs["smile"].location = player.rooms["dance floor"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["smoking room"]

    if player.time.hour == 2 and player.time.minute == 00:
        player.NPCs["couple"].location = player.rooms["dance floor"]
        player.NPCs["russian"].location = player.rooms["dance floor"]
        player.NPCs["smile"].location = player.rooms["dance floor"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["smoking room"]

    if player.time.hour == 2 and player.time.minute == 30:
        player.NPCs["couple"].location = player.rooms["dance floor"]
        player.NPCs["russian"].location = player.rooms["smoking room"]
        player.NPCs["smile"].location = player.rooms["smoking room"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["dance floor"]
        if player.NPCs["pusher"] in player.people_in_party:
            player.NPCs["pusher"].location = player.rooms["smoking room"]

    if player.time.hour == 3 and player.time.minute == 00:
        player.NPCs["couple"].location = player.rooms["smoking room"]
        player.NPCs["russian"].location = player.rooms["smoking room"]
        player.NPCs["smile"].location = player.rooms["dance floor"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["smoking room"]
        if player.NPCs["pusher"] in player.people_in_party:
            player.NPCs["pusher"].location = player.rooms["bathroom"]

    if (player.time.hour == 3 and player.time.minute == 30) or player.time.hour == 4:
        if player.party.music != "terrible":
            player.NPCs["russian"].location = player.rooms["dance floor"]
            player.NPCs["smile"].location = player.rooms["dance floor"]
            player.NPCs["couple"].location = player.rooms["dance floor"]
        elif player.party.music == "terrible":
            if (
                "Couple Convinced" not in player.memories
                or player.NPCs["couple"].convinced != True
            ):
                player.NPCs["couple"].location = player.rooms["smoking room"]
        if player.time.hour == 4 and player.time.minute == 00:
            if player.NPCs["smile"].convinced != True:
                player.NPCs["smile"].location = player.rooms["bathroom"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["dance floor"]
        if player.NPCs["pusher"] in player.people_in_party:
            player.NPCs["pusher"].location = player.rooms["bathroom"]

    if player.time.hour == 5 and player.time.minute == 00:
        # couple kisses you goodbye and leaves, removes couple from party
        if couplescenes["CoupleLeaves"].has_run != True:
            couplescenes["CoupleLeaves"].run_scene(player)
        # couple kisses you goodbye and leaves, removes couple from party
        player.NPCs["russian"].location = player.rooms["bathroom"]
        player.NPCs["smile"].location = player.rooms["dance floor"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["smoking room"]
        if player.NPCs["pusher"] in player.people_in_party:
            player.NPCs["pusher"].location = player.rooms["bathroom"]

    if player.time.hour == 5 and player.time.minute == 30:
        player.NPCs["russian"].location = player.rooms["dance floor"]
        player.NPCs["smile"].location = player.rooms["dance floor"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["dance floor"]
        if player.NPCs["pusher"] in player.people_in_party:
            player.NPCs["pusher"].location = player.rooms["bathroom"]

    ###########Then checks for condition based timed events
    if (
        (player.NPCs["tanktop"].times_talked == 1)
        and (partnerscenes["PartnerTanktop0"].has_run == False)
        and (player.location != player.NPCs["tanktop"].location)
    ):
        partnerscenes["PartnerTanktop0"].run_scene(
            player
        )  # runs partnertanktop to decide the branching path
        player.time.ten_minutes()

    elif (
        "Tanktop Partner" in player.memories
        and (player.NPCs["tanktop"].times_talked == 5)
        and (partnerscenes["PartnerTanktop5"].has_run == False)
    ):
        partnerscenes["PartnerTanktop0"].run_scene(player)
        player.time.ten_minutes()
        # run the partnertanktop hookup scene

    if player.time.hour >= 5:
        if "Gathering" in player.memories:
            player.memories.remove("Gathering")
        if "Not Gathering" in player.memories:
            player.memories.remove("Not Gathering")
        if "Music Changed" not in player.memories:
            player.memories.append("Music Not Changed")

    #################### PARTNER TUTORIALESQUE SCENES ###############

    ######BALTRI#####
    if player.high == 100:
        partnerscenes["Baltri"].run_scene(player)
    # Runs partner water is mouth is less than 30 and it hasnt run
    elif player.mouth < 30 and partnerscenes["PartnerWater"].has_run == False:
        partnerscenes["PartnerWater"].run_scene(player)

    # Runs partner Anxiety is coolness is high and it hasnt run
    elif player.coolness > 70 and partnerscenes["PartnerAnxiety"].has_run == False:
        partnerscenes["PartnerAnxiety"].run_scene(player)

    # Runs partner music is its bad and hasnt run,
    # tells you that staying on the dance floor if musics bad takes your lit down
    elif (
        player.party.music == "terrible"
        and player.location == player.rooms["dance floor"]
        and partnerscenes["PartnerMusic"].has_run == False
    ):
        partnerscenes["PartnerMusic"].run_scene(player)

    # Runs a the scene to tell you moving will take time if the partys packed.
    elif (
        player.party.crowd == "full" and partnerscenes["PartnerCrowd"].has_run == False
    ):
        partnerscenes["PartnerCrowd"].run_scene(player)

    ################################END PARTNER TUTORIALESQUE SCENES ####

    if (
        (tanktopscenes["Times4"].has_run == True)
        and (tanktopscenes["Times5"].has_run == False)
        and player.NPCs["tanktop"].location != player.rooms["dance floor"]
    ):
        player.NPCs["tanktop"].location = player.rooms[
            "dance floor"
        ]  # if tanktop4 has run and tanktop 5 hasnt run, stay there on dance floor

        if (
            player.NPCs["couple"] in player.people_in_party
            and couplescenes["CoupleGum"].has_run == False
            and player.mouth < 30
        ):
            couplescenes["CoupleGum"].run_scene(player)
