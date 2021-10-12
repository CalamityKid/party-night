from .ActionSc import Action
from ..Blocks.RoomSc import Room
from ..Format.Narration import narrate_people_in_room


class Move(Action):
    def __init__(
        self,
        name="move somewhere else",
        identifiers=["move", "go", "walk"],
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
                object_performing_the_action.NPCs[
                    "partner"
                ].location = object_to_be_interacted_with
                if object_performing_the_action.party.crowd != "full":
                    print(
                        "You and your partner move to",
                        object_to_be_interacted_with.name + ".",
                    )
                if object_performing_the_action.party.crowd == "full":
                    print(
                        " You slowly push your way through the crowd and make your way to",
                        object_to_be_interacted_with.name + ".",
                    )
                    object_performing_the_action.time.ten_minutes()
                narrate_people_in_room(object_performing_the_action)
                return (
                    None  # because time doesnt pass when you move unless crowd is full.
                )

            elif isinstance(object_to_be_interacted_with, Room) == False:
                print("You can't move to " + object_to_be_interacted_with.name + ".")
                print("You can only move to other rooms.")
                return None
        return None


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

move = Move()
