from .ActionSc import Action
from ..Blocks.ItemsSc import Item
from ..Blocks.PlayerSc import MainCharacter


class Use_Item(Action):
    def __init__(
        self,
        name="Use",
        identifiers=["use", "item", "smoke", "take", "do"],
        rooms_it_cannot_be_done_in=None,
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, object_performing_the_action, object_to_be_interacted_with):
        if isinstance(object_to_be_interacted_with, Item) != True:
            print("You can't use", object_to_be_interacted_with.name, ".")
            if isinstance(object_to_be_interacted_with, MainCharacter) == True:
                print("I mean, not in that way anyway.")
            print("You can only use the things you're holding.")
            return None
        if object_to_be_interacted_with not in object_performing_the_action.items:
            print("You don't have that on you.")
            return None
        elif object_to_be_interacted_with in object_performing_the_action.items:
            if (
                object_to_be_interacted_with
                in object_performing_the_action.active_items
            ):
                print("You've had that recently.")
                return None
            elif (
                object_to_be_interacted_with
                not in object_performing_the_action.active_items
            ):
                if (
                    object_performing_the_action.location.name
                    in object_to_be_interacted_with.rooms_it_cannot_be_done_in
                ):
                    print("You shouldn't do that in this room.")
                    return None
                object_performing_the_action.items.remove(object_to_be_interacted_with)
                print(object_to_be_interacted_with.use_text)
                object_performing_the_action.active_items[
                    object_to_be_interacted_with
                ] = object_to_be_interacted_with.duration
                return True


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

use_item = Use_Item()
