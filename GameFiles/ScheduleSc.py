from .Scripts.Blocks import NPCs, rooms, party, time, player


def update_schedule():
    ################ CROWDS #############
    if time.hour < 1 or time.hour > 5:
        party.change_crowd_empty()
    elif time.hour == 1 or time.hour == 4:
        party.change_crowd_half()
    elif time.hour == 2 or time.hour == 3:
        party.change_crowd_full()
    ################## Music ############# Must get the exception of the cutscne thingy
    if time.hour < 1 or time.hour == 2:
        party.change_music_ok()
    elif time.hour == 1 or (time.hour == 3 and time.minutes < 30):
        # if variable for music changed is FALSE:
        party.change_music_terrible()
        # otherwise make music amazing
    elif time.hour > 5:
        party.change_music_great()

    ######### characters moving around and TIMED events ###############
    if time.hour == 0 and time.minute == 00:
        NPCs["smile"].location = rooms["smoking room"]
        NPCs["russian"].location = rooms["smoking room"]
    if time.hour == 0 and time.minute == 30:
        NPCs["smile"].location = rooms["bathroom"]
        NPCs["russian"].location = player.location
        # Run scene Couple times 0
    if time.hour == 1 and time.minute == 00:
        NPCs["russian"].location = rooms["dance floor"]
        NPCs["smile"].location = rooms["smoking room"]
        NPCs["couple"].location = rooms["smoking room"]

    if time.hour == 1 and time.minute == 30:
        NPCs["couple"].location = rooms["smoking room"]
        NPCs["russian"].location = rooms["bathroom"]
        NPCs["smile"].location = rooms["dance floor"]
        if NPCs["tanktop"] in player.people_in_party:
            NPCs["tanktop"].location = rooms["smoking room"]

    if time.hour == 2 and time.minute == 00:
        NPCs["couple"].location = rooms["dance floor"]
        NPCs["russian"].location = rooms["dance floor"]
        NPCs["smile"].location = rooms["dance floor"]
        if NPCs["tanktop"] in player.people_in_party:
            NPCs["tanktop"].location = rooms["smoking room"]

    if time.hour == 2 and time.minute == 30:
        NPCs["couple"].location = rooms["dance floor"]
        NPCs["russian"].location = rooms["smoking room"]
        NPCs["smile"].location = rooms["smoking room"]
        if NPCs["tanktop"] in player.people_in_party:
            NPCs["tanktop"].location = rooms["dance floor"]
        if NPCs["pusher"] in player.people_in_party:
            NPCs["pusher"].location = rooms["smoking room"]

    if time.hour == 3 and time.minute == 00:
        NPCs["couple"].location = rooms["smoking room"]
        NPCs["russian"].location = rooms["smoking room"]
        NPCs["smile"].location = rooms["dance floor"]
        if NPCs["tanktop"] in player.people_in_party:
            NPCs["tanktop"].location = rooms["smoking room"]
        if NPCs["pusher"] in player.people_in_party:
            NPCs["pusher"].location = rooms["bathroom"]

    if (time.hour == 3 and time.minute == 30) or time.hour == 4:
        # AND you actually changed the music
        NPCs["couple"].location = rooms["dance floor"]
        NPCs["russian"].location = rooms["dance floor"]
        NPCs["smile"].location = rooms["dance floor"]
        if time.hour == 4 and time.minute == 00:
            NPCs["smile"].location = rooms["bathroom"]
        if NPCs["tanktop"] in player.people_in_party:
            NPCs["tanktop"].location = rooms["dance floor"]
        if NPCs["pusher"] in player.people_in_party:
            NPCs["pusher"].location = rooms["bathroom"]

    if time.hour == 5 and time.minute == 00:
        # couple kisses you goodbye
        NPCs["couple"].location = None
        # remove couple from people in party
        NPCs["russian"].location = rooms["bathroom"]
        NPCs["smile"].location = rooms["dance floor"]
        if NPCs["tanktop"] in player.people_in_party:
            NPCs["tanktop"].location = rooms["smoking room"]
        if NPCs["pusher"] in player.people_in_party:
            NPCs["pusher"].location = rooms["bathroom"]

    if time.hour == 5 and time.minute == 30:
        NPCs["russian"].location = rooms["dance floor"]
        NPCs["smile"].location = rooms["dance floor"]
        if NPCs["tanktop"] in player.people_in_party:
            NPCs["tanktop"].location = rooms["dance floor"]
        if NPCs["pusher"] in player.people_in_party:
            NPCs["pusher"].location = rooms["bathroom"]
