from .Scripts.Blocks.PlayerSc import player
from .Scenes.CoupleScenes.Compile import couplescenes
from .Scenes.PartnerScenes.Compile import partnerscenes


def update_schedule():
    print("People move around.")
    ################ CROWDS #############
    if player.time.hour < 1 or player.time.hour > 5:
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
        # otherwise make music amazing

    elif player.time.hour >= 5:
        player.party.change_music_great()

    ######### characters moving around and player.timeD events ###############
    if player.time.hour == 0 and player.time.minute == 00:
        player.NPCs["smile"].location = player.rooms["smoking room"]
        player.NPCs["russian"].location = player.rooms["smoking room"]
    if player.time.hour == 0 and player.time.minute == 30:
        player.NPCs["smile"].location = player.rooms["bathroom"]
        player.NPCs["russian"].location = player.location
        couplescenes["Times0"].run_scene(player)  #runs couple times 0 when its 00.30
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
        if player.time.hour == 4 and player.time.minute == 00:
            player.NPCs["smile"].location = player.rooms["bathroom"]
        if player.NPCs["tanktop"] in player.people_in_party:
            player.NPCs["tanktop"].location = player.rooms["dance floor"]
        if player.NPCs["pusher"] in player.people_in_party:
            player.NPCs["pusher"].location = player.rooms["bathroom"]

    if player.time.hour == 5 and player.time.minute == 00:
        # couple kisses you goodbye
        print("")
        print("Bye bye birdie, couple kisses you goodbye.")
        print("")
        player.NPCs["couple"].location = None
        player.people_in_party.remove(player.NPCs["couple"])
        # remove couple from people in party
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
    if (player.NPCs["tanktop"].times_talked == 1) and (couplescenes["PartnerTanktop0"].has_run == False) and (player.location != player.rooms["dance floor"]) and (player.location =! player.NPCs["tanktop"].location):
        partnerscenes["PartnerTanktop"].run_scene(player)  #runs partnertanktop to decide the branching path
        player.time.ten_minutes()
