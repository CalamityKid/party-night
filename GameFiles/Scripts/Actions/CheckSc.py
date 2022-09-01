from .ActionSc import Action
from ..Blocks.ItemsSc import Item as Item
from ..Format.Narration import narrate_actions, narrate_items


class Check(Action):
    def __init__(
        self,
        name="check something",
        identifiers=["check", "inspect", "look"],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(
        self, object_checking, thing_to_be_checked
    ):  # object checking is always the player
        print("")
        if type(thing_to_be_checked) == str:
            if thing_to_be_checked == "actions check":
                narrate_actions(object_checking)
            if thing_to_be_checked == "item check":
                narrate_items(object_checking)
            if thing_to_be_checked == "friends":
                object_checking.dict_of_actions["Talk"].narrate(object_checking)
            return None

        if type(thing_to_be_checked) != str:
            thing_to_be_checked.narrate()

        #### Item exception for narration stuff, to add more info
        if type(thing_to_be_checked) == Item:
            if thing_to_be_checked in object_checking.items:
                print("You have some on you", end="")
            elif thing_to_be_checked not in object_checking.items:
                print("You don't have any on you", end="")
            if thing_to_be_checked in object_checking.active_items:
                print(", but you've taken some recently", end="")
            print(".")
        return None

    def narrate(self, player_obj):
        print("You can also check stuff or look around.", end=" ")


check = Check()
