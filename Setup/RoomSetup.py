from ..Blocks import Room

###ROOM SETUP GOES BELOW###
# ("name" must be compatible with "the name" formula, [available actions], [usable items])
# Moods are "okay", "great music", "terrible music"###
smoking_room = Room(
    "the smoking room",
    ["[FLIRT]", "[BORROW] something", "[MOVE] to another room", "[LEAVE] the party"],
    ["lollipop", "Soundcloud", "blunt", "cigarette", "chewing gum"],
)
bathroom = Room(
    "the bathroom",
    ["[FLIRT]", "drink [TAP] water", "[MOVE] to another room", "[LEAVE] the party"],
    ["lollipop", "Soundcloud", "G", "poppers", "chewing gum"],
)
dance_floor = Room(
    "the dance floor",
    [
        "[FLIRT]",
        "[DANCE]",
        "[BORROW] something",
        "[MOVE] to another room",
        "[LEAVE] the party",
    ],
    ["lollipop", "Soundcloud", "poppers", "chewing gum"],
)

every_room = [smoking_room, bathroom, dance_floor]
# remember to add borrow to the actions available in rooms in the tutorial
###ROOM SETUP ABOVE, Every new room must also be set up in Battle.move()###

print(smoking_room)
