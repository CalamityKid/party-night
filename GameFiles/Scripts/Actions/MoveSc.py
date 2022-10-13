from time import sleep
from .ActionSc import Action
from ..Blocks.RoomSc import Room

from ..Format.formatting import format_objects_string


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
            sleep(2)
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
                print(" ")
                sleep(2)

                return None
                # because time doesnt pass when you move unless crowd is full.

            elif isinstance(object_to_be_interacted_with, Room) == False:
                print("You can't move to " + object_to_be_interacted_with.name + ".")
                print("You can only move to other rooms.")
                return None
        return None

    def narrate(self, player_obj):
        move_string = "You could [MOVE] to "
        move_list = []
        for key, room in player_obj.rooms.items():
            if room != player_obj.location:
                move_list.append(room.name)
        move_string += format_objects_string(move_list)
        move_string = move_string.replace("and", "or")
        print(move_string)
        sleep(2)


#########################################################################
#############################   INSTANCES   #############################
#########################################################################

move = Move()
