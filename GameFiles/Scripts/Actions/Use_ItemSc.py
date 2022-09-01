from .ActionSc import Action
from ..Blocks.ItemsSc import Item, items
from ..Blocks.PlayerSc import MainCharacter
from ..Format.formatting import format_objects_string


class Use_Item(Action):
    def __init__(
        self,
        name="use something you're holding",
        identifiers=["use", "item", "smoke", "take", "do"],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, object_performing_the_action, object_to_be_interacted_with):
        if isinstance(object_to_be_interacted_with, Item) != True:
            print("You can't use", object_to_be_interacted_with.name + ".")
            if isinstance(object_to_be_interacted_with, MainCharacter) == True:
                print("I mean, not like that anyway.")
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
                ########### poppers exception cause time passes if you use poppers
                # if object_to_be_interacted_with == items["poppers"]:
                #    return True
                return True

    def narrate(self, player_obj):
        unusable_item_list = []
        final_string = ""
        if len(player_obj.items) == 0:
            final_string = "You don't have any items you can [USE] atm."
        elif len(player_obj.items) > 0:
            final_string += "You can't [USE] "
        for i in player_obj.items:
            if i.usable_in_room(player_obj.location) == False:
                unusable_item_list.append(i)

        if len(unusable_item_list) > 0:
            final_string += format_objects_string(unusable_item_list)
            final_string = final_string.replace("and", "or")
            final_string = final_string.replace(" a ", " the ")
            final_string = final_string.replace(".", " in this room though.")

        if len(player_obj.items) > 0:
            print(
                "You have "
                + (format_objects_string(player_obj.items)[:-1])
                + " in your pockets."
            )

        elif len(player_obj.items) == 0:
            print("You're not holding anything rn.")

        if len(final_string) >= 34:
            print(final_string)


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

use_item = Use_Item()
