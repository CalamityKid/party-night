#####REMEMBER.
# remeber to add people to player.people_in_party in Scenes when they are introduced
# Give "Tanktop Hookup" memory in flirt, the two of you hook up with them, also Tanktop Home and gameover
# fix borrow to only include the people in the room!
# Attending Film Festival and Not Attending Film Festival to russian game over
# write partnerdance, write changed music
# Write convinced scenes. couple? if its 4.30 am and the music is great and couple is in smoking room, move couple to dance floor and do a transition next, make times talked 4>>

# Link balti #plays immediately when your high goes up to 100
# in schedule, if its 5 and music changed not in memories and gathering in memories, "DJ changes", add music not changed to memories
# Get the flow down properly in partner and the gather scenes

# TO DO
# # aslo Smile use G has too many spaces.
# consider making a save function.

# MAYBE
# Narrate everything before each turn, make text more interactive, maybe make it a setting.

# in dance
# the stats are all fucked up but I modified a lot of player stats so we gotta check that as well

# check if the Tanktop dance thing, flirt > 5 is ok or not

# body update or something is out of control
# theres a cool loop also, it cannot go down at all, its forever high, maybe bad dance should really get it down


def partnertimes1content(player):
    sleep(2)
    player.modify_stat("lit", 10, True)
    player.NPCs["partner"].times_talked = 2
    return True
