from .ActionSc import Action
from ..Blocks.ItemsSc import Item as Item
from ..Blocks.NPCSc import NPC as NPC
from ...Scenes.BorrowScenes.Compile import borrow_scenes, item_redirect


class Borrow(Action):
    def __init__(
        self,
        name="borrow something from a friend",
        identifiers=[
            "borrow",
            "ask",
        ],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(
        self, object_checking, thing_to_be_checked
    ):  # object checking is always the player
        print("")

        namestr = thing_to_be_checked.name

        if type(thing_to_be_checked) == NPC or type(thing_to_be_checked) == Item:

            if type(thing_to_be_checked) == Item:
                if namestr in item_redirect:
                    namestr = item_redirect[namestr]

                    for key, item in object_checking.NPCs.items():
                        if item.name == namestr:
                            thing_to_be_checked = item

            if type(thing_to_be_checked) == NPC:
                if thing_to_be_checked.location != object_checking.location:
                    print("You don't see", thing_to_be_checked.name, "around.")
                    return None

            for key, item in borrow_scenes.items():
                if namestr in key:
                    return borrow_scenes[key].run_scene(object_checking)

        print("You haven't been offered " + thing_to_be_checked.name + ".")
        return None


borrow = Borrow()
