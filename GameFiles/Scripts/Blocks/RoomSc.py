from .PlayerSc import player


class Room:
    def __init__(self, name, available_actions, usable_items, identifiers):
        self.name = name
        self.available_actions = available_actions
        self.usable_items = usable_items
        self.identifiers = identifiers

    def __repr__(self):
        return self.name

    def narrate(self):

        if player.location != self:
            print(
                "You're not in " + str(self.name) + ". You could move there. ", end=" "
            )
        if self.name == "the dance floor":
            print(
                "You and your partner are currently on "
                + str(player.location.name)
                + "."
            )
        else:
            print(
                "You and your partner are currently in "
                + str(player.location.name)
                + "."
            )
        player.dict_of_actions["Talk"].narrate(player)

    def usable_in_room(self, object):
        try:
            if object.name in self.usable_items:
                return True
            elif object.name not in self.usable_items:
                return False
        except TypeError:
            return True


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

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
