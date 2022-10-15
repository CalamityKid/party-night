from .ActionSc import Action
from ..Blocks.ItemsSc import Item as Item
from ..Blocks.NPCSc import NPC as NPC
from ...Scenes.BorrowScenes.Compile import borrow_scenes
from ..Format.BorrowCalculations import (
    item_redirect,
    available_borrows,
    remove_if_not_here,
)
from ..Format.formatting import format_objects_string


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
        unaltered_namestr = thing_to_be_checked.name
        identified_NPC = None
        input_was_NPC = None

        if type(thing_to_be_checked) == NPC:
            identified_NPC = True
            input_was_NPC = True

            # since borrow scenes are linked to names of people, there's a dictionary
            # called item_redirect in BorrowCompile that returns the name of the character
            # whose item is being borrowed if items are written
        elif type(thing_to_be_checked) == Item:
            if namestr in item_redirect:
                namestr = item_redirect[namestr]

                # reassigns thing to be checked to the NPC object
                for key, item in object_checking.NPCs.items():
                    if item.name == namestr:
                        thing_to_be_checked = item
                        identified_NPC = True

        if identified_NPC == True:

            # runs available borrows to check if you can run that scene or not, if its in player memory
            memory_list = available_borrows(object_checking)
            # print("the available borrows list is now", memory_list)

            for key, item in borrow_scenes.items():
                if namestr in key:  # The Scene Exists in Borrow Scene Dictionary
                    # print("yes, it's inside of the borrow scene dict")
                    memory_list = available_borrows(object_checking)

                    if namestr in memory_list:  # AND it exists in Player Memories
                        # print("and it's inside player memories")

                        if (
                            thing_to_be_checked.location == object_checking.location
                        ):  # check for location
                            return borrow_scenes[key].run_scene(
                                object_checking
                            )  # run the scene
                        else:  # they're not here
                            print("You don't see", thing_to_be_checked.name, "around.")
                            return None

        # print("not in player memories OR any other situation")
        if input_was_NPC:
            print("You haven't been offered anything by " + unaltered_namestr + ".")
            return None
        print("You haven't been offered " + unaltered_namestr + ".")
        return None

    def narrate(self, player_obj):
        print("")
        final_str = "You could [BORROW] "
        borrow_list = available_borrows(player_obj)
        borrow_list = remove_if_not_here(borrow_list, player_obj)
        str_list = []
        if len(borrow_list) > 0:
            for i in borrow_list:
                for item, person in item_redirect.items():
                    if i in person:
                        str_list.append(
                            "{thing} from {someone}".format(thing=item, someone=person)
                        )
            final_str = final_str + format_objects_string(str_list)
            final_str = final_str.replace("and", "or")
            print(final_str[:-1] + ".")


borrow = Borrow()
