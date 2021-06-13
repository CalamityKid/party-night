from .ActionSc import Action
from ..Blocks.RoomSc import Room
from ..Format.Narration import narrate_people_in_room


class Move(Action):
    def __init__(
        self,
        name="move somewhere else",
        identifiers=["move", "go"],
        rooms_it_cannot_be_done_in=[],
    ):
        self.name = name
        self.identifiers = identifiers
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def execute(self, object_performing_the_action, object_to_be_interacted_with):

        if object_performing_the_action.location == object_to_be_interacted_with:
            print("You're already in this room.")
            return None
        elif object_performing_the_action.location != object_to_be_interacted_with:
            if isinstance(object_to_be_interacted_with, Room) == True:
                object_performing_the_action.location = object_to_be_interacted_with
                print(
                    object_performing_the_action.name,
                    "moves to",
                    object_to_be_interacted_with.name + ".",
                )
                narrate_people_in_room(object_performing_the_action)
                return True

            elif isinstance(object_to_be_interacted_with, Room) == False:
                print("You can't move to " + object_to_be_interacted_with.name + ".")
                print("You can only move to other rooms.")
                return None
        return None


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

move = Move()
