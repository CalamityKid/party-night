class Room:
    def __init__(self, name, available_actions, usable_items):
        self.name = name
        self.available_actions = available_actions
        self.usable_items = usable_items

    def __repr__(self):
        return self.name


###ROOM SETUP GOES BELOW###
# ("name" must be compatible with "the name" formula, [available actions], [usable items])
# Every new room must also be set up in Battle.move()###
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
###ROOM SETUP ABOVE#####################################################
