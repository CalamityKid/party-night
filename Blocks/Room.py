class Room:
    def __init__(self, name, available_actions, usable_items, identifiers):
        self.name = name
        self.available_actions = available_actions
        self.usable_items = usable_items
        self.identifiers = identifiers

    def __repr__(self):
        return self.name


###ROOM SETUP GOES BELOW###
# ("name" must be compatible with "the name" formula, [available actions], [usable items])
# Every new room must also be set up in Battle.move()###
smoking_room = Room(
    "the smoking room",
    ["[FLIRT]", "[BORROW] something", "[MOVE] to another room", "[LEAVE] the party"],
    ["lollipop", "Soundcloud", "blunt", "cigarette", "chewing gum"],
    ["smok"],
)
bathroom = Room(
    "the bathroom",
    ["[FLIRT]", "drink [TAP] water", "[MOVE] to another room", "[LEAVE] the party"],
    ["lollipop", "Soundcloud", "G", "poppers", "chewing gum"],
    ["bath"],
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
    ["danc", "floor"],
)

every_room = [smoking_room, bathroom, dance_floor]
rooms = {"smoking room": smoking_room, "bathroom": bathroom, "dance floor": dance_floor}
