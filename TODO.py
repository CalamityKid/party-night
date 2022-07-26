#####REMEMBER.
# remeber to add people to player.people_in_party in Scenes when they are introduced
# partner gives you "Borrow" memory. This is now unnecesary.
# Give "Tanktop Hookup" memory in flirt, the two of you hook up with them, also Tanktop Home and gameover
# Make partner anxiety, crowd, music, water run automatically
# "Ask for k" in memories. Ask for. "Ask for P"  "Ask for G" in memories. Borrow Gum, no memory.
# probable circular import in partnerstimes2 and in partnergather con el compile de partnerscenes
# fix the code in partnerdance
# Attending Film Festival and Not Attending Film Festival to russian game over
# dance can take 20 minutes
# add tanktop and partner flirt scenes

# Link balti #plays immediately when your high goes up to 100
# make script for friends on dance floor to check for the gathering scene, in partnerdance
# in schedule, if its 5 and music changed not in memories and gathering in memories, "DJ changes", add music not changed to memories
# Get the flow down properly in partner and the gather scenes

# TO DO
# # aslo Smile use G has too many spaces.
# consider making a save function.

# MAYBE
# Narrate everything before each turn, make text more interactive, maybe make it a setting.

# in dance
# consider making a formatting function that edits the length of sentences before theyre printed.
# the stats are all fucked up but I modified a lot of player stats so we gotta check that as well

# check if the Tanktop dance thing, flirt > 5 is ok or not

# body update or something is out of control
# theres a cool loop also, it cannot go down at all, its forever high, maybe bad dance should really get it down

# the list of people in room is being calculated multiple times, maybe make it more efficient


def partnertimes1content(player):
    sleep(2)
    player.modify_stat("lit", 10, True)
    player.NPCs["partner"].times_talked = 2
    return True
