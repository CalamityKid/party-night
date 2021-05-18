from Blocks.Room import Room, rooms
from Blocks.PlayerNPC import player, NPCs


class Action:
    def __init__(
        self,
        name,
        identifiers,
        rooms_it_cannot_be_done_in=None,
    ):
        self.name = name
        self.identifiers = identifiers
        # self.object_performing_the_action = object_performing_the_action
        # self.object_to_be_interacted_with = object_to_be_interacted_with
        # Maybe these arent necesary actually
        self.rooms_it_cannot_be_done_in = rooms_it_cannot_be_done_in

    def __repr__(self):
        return ("the action ", self.name)


class Move(Action):
    pass

    def move(object_performing_the_action, object_to_be_interacted_with):

        if object_performing_the_action.location == object_to_be_interacted_with:
            print("You're already in this room.")
            return None
        elif object_performing_the_action.location != object_to_be_interacted_with:
            if isinstance(object_to_be_interacted_with, Room) == True:
                object_performing_the_action.location = object_to_be_interacted_with
                print(
                    object_performing_the_action.name,
                    "moves to ",
                    object_to_be_interacted_with.name + ".",
                )
            elif isinstance(object_to_be_interacted_with, Room) == False:
                print("DEBUGGING the object you passed is NOT a room.")
                return None


moveinstance = Move("move instance", "move")
# Move.move(player, rooms["dance floor"]) THIS WORKS FINE

# if isinstance(rooms["smoking room"], Room) == True:
#    print("yus")
